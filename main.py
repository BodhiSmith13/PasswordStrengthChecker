import enchant

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

# For every character in the string, start there. From there, iterate up the string, building a larger substring
# every time. If the substring is a word, save it. Once every character has been through this process, rearrange all words
# until a sentence is formed. Then, remove all spaces from that sentence, and compare it to the input. If they are the same
#, an appropriate pass phrase has been inputted

def is_phrase (string):
    if not string.isalpha():
        return False
    words = []
    i = 0
    while i < len(string) + 1:
        j = i
        while j < len(string) + 1:
            if ((string[i:j] != "" and
            d.check(string[i:j])) and
            (len(string[i:j]) > 1 or string[i:j].lower() == "i" or string[i:j].lower() == "a")):
                words.append(string[i:j])
            j += 1
        i += 1

    if debug:
        print(f"Words found in password:")
        print(", ".join(words))

    starter_words = []
    for word in words:
        if word[0] == string[0]:
            starter_words.append(word)
    starter_words = list(dict.fromkeys(starter_words))

    if debug:
        print("Words found in password that begin with the first character of the password:")
        print(", ".join(starter_words))
    if len(starter_words) > 0:
        for starter_word in starter_words:
            result = build_phrase(words, starter_word, string)
            if result:
                if debug:
                    print(f"Found a phrase that matches the inputted password\n")
                return True
        return False
    else:
        return False


def build_phrase (words, starter_word, string):
    new_words = []
    if debug:
        print(f"Starting with {"".join(starter_word)}")
    i = 0
    for word in words:
        i += 1
        if debug:
            print(f"Looking at {word}, word {i} in the word list")
        if string[0:len(starter_word + word)] == starter_word + word:
            if debug:
                print(f"Appending {word}")
            new_words.append(starter_word + word)
            if debug:
                print(f"{string[0:len(new_words[-1])]} matches {new_words[-1]}")
    if debug:
        print(", ".join(new_words))
    if string in new_words:
        return True
    for new_word in new_words:
        result = build_phrase(words, new_word, string)
        if result:
            return result
    return False

if not debug:
    debug = input("Do you want debug enabled? Input anything for yes, or press enter to continue.")

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

    # Initializes lists of punctuation and symbol characters
    punctuationList = ['.', '!', '?', ',', ';', ':', "\"", "\'"]
    symbolList = ['@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=']

    # Initializes individual counting and scoring metrics
    lowercase = 0
    uppercase = 0
    digits = 0
    punctuation = 0
    symbols = 0
    unidentified = 0
    unidentifiedCombo = 0
    totalCombos = 0
    score = 0

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
        unidentifiedCombo = (95 - 52 - 10 - len(punctuationList) - len(symbolList)) ** unidentified

    # Tells the user how much of each character type their password has
    print("\nYour password has:\n"
          f"{lowercase} lowercase letters\n"
          f"{uppercase} uppercase letters\n"
          f"{digits} digits\n"
          f"{punctuation} punctuation\n"
          f"{symbols} symbols\n"
          f"{unidentified} unidentified characters\n")

    # For each character type, checks if that character type is present. If so, then calculates the total number of
    # combinations based on the amount of that character type and the total number of varieties of that character
    charset_size = 0
    if lowercase: charset_size += 26
    if uppercase: charset_size += 26
    if digits: charset_size += 10
    if punctuation: charset_size += len(punctuationList)
    if symbols: charset_size += len(symbolList)
    if unidentified: charset_size += unidentifiedCombo
    if debug:
        print(f"Charset size: {charset_size}\n")
    totalCombos = charset_size ** len(password)

    #Checks if length of password is less than 15
    if len(password) >= 15:
        print(f"Your password is {len(password)} characters long. This is great!\n")
        score += 3
    else:
        print(f"Your password is {len(password)} characters long. This is too short.\n")

    if is_phrase(password):
        print("Your password is a passphrase.\n")
        score += 2
    else:
        print("Your password is not a passphrase.\n")

    # Checks if the password contains only letters
    if password.isalpha():
        print("Your password contains only letters. This is acceptable.\n")
    elif password.isdigit():
        print("Your password contains only digits. This is not good.\n")
    elif password.isalnum():
        print("Your password contains only alphanumeric characters. This is acceptable.\n")
    else:
        print("Your password contains a variety of characters. This is great!\n")
        score += 1

    print(f"Your password has {totalCombos:,} possible combinations.\n")
    crack_time(totalCombos)

    print(f"Your password has scored {score} out of 5 possible points.\n")

    if score > 3:
        print(f"Your password {password} is acceptable.")
        break
    else:
        print(f"Your password {password} is rejected.\n")


