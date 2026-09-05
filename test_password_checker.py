import time

import pytest
from main import score_password, is_phrase

def test_short_digit_only_password_scores_zero():
    result = score_password("1234")
    assert result["digits"] == 4
    assert result["score"] == 0

def test_long_passphrase_scores_five():
    result = score_password("Sharksseekblood")
    assert result["score"] == 5

def test_length_bonus_awarded_at_15_chars():
    result = score_password("a" * 15)
    assert result["score"] >= 3

def test_length_bonus_not_awarded_under_15_chars():
    result = score_password("a" * 14)
    result_score_without_length = result["score"]
    assert result_score_without_length < 3 or is_phrase("a" * 14) is False

def test_variety_bonus_requires_mixed_types():
    result = score_password("abc123!@#")
    assert result["score"] >= 1

def test_empty_password_does_not_crash():
    result = score_password("")
    assert result["total_combos"] == 0

def test_is_phrase_detects_valid_passphrase():
    assert is_phrase("catandhat") is True

def test_is_phrase_rejects_broken_chain():
    assert is_phrase("catfcat") is False

def test_is_phrase_rejects_non_alpha():
    assert is_phrase("cat123") is False

def test_character_counting_accuracy():
    result = score_password("Ab1!#`")
    assert result["lowercase"] == 1
    assert result["uppercase"] == 1
    assert result["digits"] == 1
    assert result["punctuation"] == 1
    assert result["symbols"] == 1
    assert result["unidentified"] == 1

def test_is_phrase_completes_quickly_on_overlapping_substrings():
    """
    Regression test for the exponential blowup in the old recursive
    build_phrase implementation. This string has many overlapping short
    dictionary substrings (ants, ant, at, sat, ...), which caused the
    unmemoized version to hang. The DP version should resolve it near-instantly.
    """
    start = time.perf_counter()
    result = is_phrase("antsatsatsatsrunfast")
    elapsed = time.perf_counter() - start

    assert elapsed < 1.0, f"is_phrase took {elapsed:.2f}s — possible regression to exponential blowup"
    # Not asserting on `result` itself here since we don't know their exact
    # dictionary output; the point of this test is speed, not correctness.

def test_unidentified_character_entropy_is_not_double_exponentiated():
    """
    Regression test for a bug where unidentified characters' combination
    count was calculated as (alphabet_size ** count), then that already-
    exponentiated number was treated as an alphabet size and exponentiated
    again by the full password length — wildly inflating the result.
    """
    password = "a\u2022\u00b1"  # 1 lowercase letter + 2 unidentified symbols (•, ±)
    result = score_password(password)

    # Expected: alphabet size = 26 (lowercase) + 14 (unidentified bucket) = 40
    # Correct total combos = 40 ** len(password) = 40 ** 3 = 64,000
    expected_combos = 40 ** 3

    assert result["total_combos"] == expected_combos, (
        f"Expected {expected_combos:,} combinations, got {result['total_combos']:,} "
        f"— check for double-exponentiation of the unidentified character bucket"
    )