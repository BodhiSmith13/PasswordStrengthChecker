import enchant
import argparse

debug = False
d = enchant.Dict("en_US")
# Calculates how long it would take to crack password and uses appropriate units
def crack_time (combos):
    print("The average computer can make 100 billion attempts a second at cracking your password.")
    time_to_guess = combos / 100000000000
    if time_to_guess >= 3154000000:
        print(f"It would take the average computer {time_to_guess / 3154000000:,.4f} centuries at most to guess your "
              f"password.\nOn average, it would take {time_to_guess / 3154000000 / 2:,.4f} centuries.\n")
    elif time_to_guess >= 315400000:
        print(f"It would take the average computer {time_to_guess / 315400000:,.4f} decades at most to guess your "
              f"password.\nOn average, it would take {time_to_guess / 315400000 / 2:,.4f} decades.\n")
    elif time_to_guess >= 31540000:
        print(
            f"It would take the average computer {time_to_guess / 31540000:,.4f} years at most to guess your password."
            f"\nOn average, it would take {time_to_guess / 31540000 / 2:,.4f} years.\n")
    elif time_to_guess >= 2628000:
        print(
            f"It would take the average computer {time_to_guess / 2628000:,.4f} months at most to guess your password."
            f"\nOn average, it would take {time_to_guess / 2628000 / 2:,.4f} months.\n")
    elif time_to_guess >= 604800:
        print(
            f"It would take the average computer {time_to_guess / 604800:,.4f} weeks at most to guess your password.\n"
            f"On average, it would take {time_to_guess / 604800 / 2:,.4f} weeks.\n")
    elif time_to_guess >= 86400:
        print(f"It would take the average computer {time_to_guess / 86400:,.4f} days at most to guess your password\n"
              f"On average, it would take {time_to_guess / 86400 / 2:,.4f} days.\n")
    elif time_to_guess >= 3600:
        print(f"It would take the average computer {time_to_guess / 3600:,.4f} hours at most to guess your password\n"
              f"On average, it would take {time_to_guess / 3600 / 2:,.4f} hours.\n")
    elif time_to_guess >= 60:
        print(f"It would take the average computer {time_to_guess / 60:,.4f} minutes at most to guess your password\n"
              f"On average, it would take {time_to_guess / 60 / 2:,.4f} minutes.\n")
    else:
        print(f"It would take the average computer {time_to_guess:,.4f} seconds at most to guess your password.\n"
              f"On average, it would take {time_to_guess / 2:,.4f} seconds.\n")

# Create a boolean array `reachable`, sized one longer than the password, with every
# index False except index 0 (True, since an empty prefix is trivially reachable).
#
# For each i from 1 to len(password):
#   For each j from 0 to i-1:
#     Skip this j if reachable[j] is False — only extend from prefixes already
#     proven reachable.
#     Otherwise, take the substring password[j:i]. If it's longer than 1 character
#     (or is "a"/"i"), and it's a valid English word, mark reachable[i] = True and
#     stop checking further j's for this i.
#   If no valid word was found for any j, reachable[i] stays False.
#
# After the loops, reachable[n] tells us whether the whole password can be built
# from a chain of dictionary words.

def is_phrase (string):
    if not string.isalpha():
        return False
    n = len(string)
    reachable = [False] * (n + 1)
    reachable[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if not reachable[j]:
                continue
            substring = string[j:i]
            is_valid_single = len(substring) > 1 or substring.lower() in ("a", "i")
            if is_valid_single and d.check(substring):
                reachable[i] = True
                break

    if debug:
        print(f"Reachable prefix lengths: {[i for i in range(n+1) if reachable[i]]}")

    return reachable[n]

def score_password(password):

    punctuationList = ['.', '!', '?', ',', ';', ':', "\"", "\'"]
    symbolList = ['@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']
    # Initializes individual counting and scoring metrics
    lowercase = uppercase = digits = punctuation = symbols = unidentified = unidentifiedAlphabetSize = 0
    isPassphrase = False

    # Tallies the number of characters present of each type
    for char in password:
        if char.isalpha() and char.islower():
            lowercase += 1
        elif char.isalpha() and char.isupper():
            uppercase += 1
        elif char.isdigit():
            digits += 1
        elif char in punctuationList:
            punctuation += 1
        elif char in symbolList:
            symbols += 1
        else:
            unidentified += 1
    if unidentified != 0:
        unidentifiedAlphabetSize = (95 - 52 - 10 - len(punctuationList) - len(symbolList))

    # For each character type, checks if that character type is present. If so, then calculates the total number of
    # combinations based on the amount of that character type and the total number of varieties of that character
    charset_size = 0
    if lowercase: charset_size += 26
    if uppercase: charset_size += 26
    if digits: charset_size += 10
    if punctuation: charset_size += len(punctuationList)
    if symbols: charset_size += len(symbolList)
    if unidentified: charset_size += unidentifiedAlphabetSize
    total_combos = charset_size ** len(password) if password else 0

    score = 0
    if len(password) >= 15:
        score += 3

    if is_phrase(password):
        isPassphrase = True
        score += 2

    charTypes = [lowercase, uppercase, digits, punctuation, symbols, unidentified]
    if not isPassphrase:
        charCount = 0
        for i in charTypes:
            if i > 0:
                charCount += 1
        if charCount >= 3:
            score += 1

    return {
        "lowercase": lowercase, "uppercase": uppercase, "digits": digits,
        "punctuation": punctuation, "symbols": symbols, "unidentified": unidentified,
        "total_combos": total_combos, "score": score,
    }

def main():

    global debug
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()


    # Introductory message
    print("Welcome to Password Strength Checker! Your goal is to create a five star password.")
    print("Password guidelines (ranked in order of how many points they give):\n"
          "1. Make your password a passphrase, such as \"Sharksseekblood.\"\n"
          "2. Make your password at least 15 characters long.\n"
          "3. Include a variety of character types.\n")

    # Loops until the user decides to exit
    while True:

        # Asks user for password
        password = input("Enter your password, or enter exit to cancel: ")
        if password.lower() == "exit":
            break

        result = score_password(password)

        print("\nYour password has:\n"
              f"{result['lowercase']} lowercase letters\n"
              f"{result['uppercase']} uppercase letters\n"
              f"{result['digits']} digits\n"
              f"{result['punctuation']} punctuation\n"
              f"{result['symbols']} symbols\n"
              f"{result['unidentified']} unidentified characters\n")

        print(f"Your password has {result['total_combos']:,} possible combinations.\n")
        crack_time(result['total_combos'])

        print(f"Your password has scored {result['score']} out of 5 possible stars.\n")

        if float(result['score']) > 3:
            print(f"Your password {password} is acceptable.")
            break
        else:
            print(f"Your password {password} is rejected.\n")

if __name__ == "__main__":
    main()