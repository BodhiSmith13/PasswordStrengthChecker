# Password Strength Checker

A command-line tool that analyzes the strength of a password and scores it out of 5 stars based on length, character variety, and whether it's a passphrase. Rather than relying on arbitrary rules, it estimates the actual number of possible combinations for a given password and converts that into a human-readable "time to crack" estimate.

## How it works

1. **Character analysis** — the password is scanned and each character is classified into one of six types: lowercase letters, uppercase letters, digits, punctuation, symbols, or unidentified (other) characters.
2. **Combination count** — for each character type present, its alphabet size (e.g. 26 for lowercase letters) is added to a running total. The total number of possible combinations is then calculated as `alphabet_size ^ password_length`.
3. **Crack time estimate** — that combination count is compared against an estimated average computer's guessing speed (100 billion attempts/second) to produce a human-readable "time to crack" figure (seconds up to centuries).
4. **Passphrase detection** — the password is checked to see if it can be fully decomposed into a chain of valid English dictionary words (e.g. `"sharksseekblood"` → `"sharks"` + `"seek"` + `"blood"`), using a dynamic-programming word-break algorithm.
5. **Scoring** — points are awarded as follows:
   - **+3** if the password is at least 15 characters long
   - **+2** if the password is a valid passphrase
   - **+1** if the password contains at least 3 of the 6 character types (and isn't already a passphrase)
   - A score **above 3** is considered acceptable; otherwise the program asks for another password.

## Example output

```
Welcome to Password Strength Checker! Your goal is to create a five star password.
Password guidelines (ranked in order of how many points they give):
1. Make your password a passphrase, such as "Sharksseekblood."
2. Make your password at least 15 characters long.
3. Include a variety of character types.

Enter your password, or enter exit to cancel: 1234

Your password has:
0 lowercase letters
0 uppercase letters
4 digits
0 punctuation
0 symbols
0 unidentified characters

Your password has 10,000 possible combinations.

The average computer can make 100 billion attempts a second at cracking your password.
It would take the average computer 0.0000 seconds at most to guess your password.
On average, it would take 0.0000 seconds.

Your password has scored 0 out of 5 possible stars.

Your password 1234 is rejected.

Enter your password, or enter exit to cancel: sharksseekblood

Your password has:
15 lowercase letters
0 uppercase letters
0 digits
0 punctuation
0 symbols
0 unidentified characters

Your password has 1,677,259,342,285,725,925,376 possible combinations.

The average computer can make 100 billion attempts a second at cracking your password.
It would take the average computer 5.3179 centuries at most to guess your password.
On average, it would take 2.6589 centuries.

Your password has scored 5 out of 5 possible stars.

Your password sharksseekblood is acceptable.
```

## Installation

Requires Python 3.10+.

1. Clone the repository:
   ```bash
   git clone https://github.com/BodhiSmith13/PasswordStrengthChecker.git
   cd PasswordStrengthChecker
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

   This project uses [`pyenchant`](https://pyenchant.github.io/pyenchant/) for dictionary lookups during passphrase detection. `pyenchant` requires a system-level spell-checking backend in addition to the Python package:

   | OS | Command |
   |---|---|
   | Windows | Download the standalone `enchant` binary from the [pyenchant releases page](https://github.com/pyenchant/pyenchant/releases) |
   | macOS | `brew install enchant` |
   | Linux (Debian/Ubuntu) | `sudo apt install enchant-2` |

## Usage

Run the program from the command line:

```bash
python main.py
```

Enable verbose debug output (shows internal character-set sizes, passphrase-detection prefix reachability, etc.):

```bash
python main.py --debug
```

Enter a password when prompted, or type `exit` to quit. The program will keep prompting until a password scores above 3 stars.

## Running tests

Tests are written with [`pytest`](https://docs.pytest.org/):

```bash
python -m pip install pytest
python -m pytest test_password_checker.py -v
```

The test suite covers scoring accuracy, character counting, passphrase detection (including edge cases like adjacent valid words separated by a single invalid character, e.g. `"catfcat"`), and two regression tests specifically guarding against bugs found during development:
- An early implementation of passphrase detection used unmemoized recursion and could hang on inputs with many overlapping dictionary substrings; a timing test guards against this reappearing.
- An early version of the entropy calculation double-counted unidentified characters' combination count; a regression test locks in the corrected math.

## Known limitations

- Passphrase detection currently only supports the `en_US` dictionary via `pyenchant`.
- The "unidentified character" alphabet size is a fixed estimate based on printable ASCII; it does not dynamically size for other Unicode ranges (e.g. emoji, non-Latin scripts).
- `pyenchant` requires a system-level binary as noted above, which adds a setup step beyond a plain `pip install`.

## Guidelines source

Password strength guidelines were informed by [NIST's password guidance](https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password).
