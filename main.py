import enchant

d = enchant.Dict("en_US")
# Calculates how long it would take to crack password and uses appropriate units
def crack_time (combos):
    print("The average computer can make 100 billion attempts a second at cracking your password.")
    time_to_guess = combos / 100000000000
    if time_to_guess < 60:
        print(f"It would take the average computer {time_to_guess:,.4f} seconds at most to guess your password.\n"
              f"On average, it would take {time_to_guess / 2:,.4f} seconds.")
    elif time_to_guess >= 3154000000:
        print(f"It would take the average computer {time_to_guess / 3154000000:,.4f} centuries at most to guess your "
              f"password.\nOn average, it would take {time_to_guess / 3154000000 / 2:,.4f} centuries.")
    elif time_to_guess >= 315400000:
        print(f"It would take the average computer {time_to_guess / 315400000:,.4f} decades at most to guess your "
              f"password.\nOn average, it would take {time_to_guess / 315400000 / 2:,.4f} decades.")
    elif time_to_guess >= 31540000:
        print(
            f"It would take the average computer {time_to_guess / 31540000:,.4f} years at most to guess your password."
            f"\nOn average, it would take {time_to_guess / 31540000 / 2:,.4f} years.")
    elif time_to_guess >= 2628000:
        print(
            f"It would take the average computer {time_to_guess / 2628000:,.4f} months at most to guess your password."
            f"\nOn average, it would take {time_to_guess / 2628000 / 2:,.4f} months.")
    elif time_to_guess >= 604800:
        print(
            f"It would take the average computer {time_to_guess / 604800:,.4f} weeks at most to guess your password.\n"
            f"On average, it would take {time_to_guess / 604800 / 2:,.4f} weeks.")
    elif time_to_guess >= 86400:
        print(f"It would take the average computer {time_to_guess / 86400:,.4f} days at most to guess your password\n"
              f"On average, it would take {time_to_guess / 86400 / 2:,.4f} days.")
    elif time_to_guess >= 3600:
        print(f"It would take the average computer {time_to_guess / 3600:,.4f} hours at most to guess your password\n"
              f"On average, it would take {time_to_guess / 3600 / 2:,.4f} hours.")
    elif time_to_guess >= 60:
        print(f"It would take the average computer {time_to_guess / 60:,.4f} minutes at most to guess your password\n"
              f"On average, it would take {time_to_guess / 60 / 2:,.4f} minutes.")

# For every character in the string, start there. From there, iterate up the string, building a larger substring
# every time. If the substring is a word, save it. Once every character has been through this process, rearrange all words
# until a sentence is formed. Then, remove all spaces from that sentence, and compare it to the input. If they are the same
#, an appropriate pass phrase has been inputted

def display_list (array):
    for item in array:
        print(item, end=", ")
    print()

def mash (array):
    string = ""
    for item in array:
        string += item
    return string

def remove_duplicants (array):
    i = 0
    output = []
    while i < len(array) - 1:
        if array[i] not in output:
            output.append(array[i])
        i += 1
    return output

def is_phrase (string):
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

    display_list(words)

    starter_words = []
    for word in words:
        if word[0] == string[0]:
            starter_words.append(word)
    starter_words = remove_duplicants(starter_words)

    display_list(starter_words)
    for starter_word in starter_words:
        build_phrase(words, starter_word, string)


def build_phrase (words, starter_word, string):
    phrase = [starter_word]
    print(f"Starting with {mash(starter_word)}")
    i = 0
    for word in words:
        i += 1
        print(f"Looking at {word}, word {i} in the word list")
        if string[0:len(mash(phrase) + word)] == mash(phrase) + word:
            print(f"Appending {word}")
            phrase.append(word)
            print(f"{string[0:len(mash(phrase))]}:{mash(phrase)}")
            build_phrase(words, mash(phrase), string)
            break
    return ""



test = "isitin"
is_phrase(test)


# Introductory message
print("Password guidelines:\n"
      "1. Make your password at least 15 characters long.\n"
      "2. Include a variety of character types.\n"
      "3. Avoid passwords that are entirely numbers.\n")

# Loops until the user decides to exit
while True:

    # Asks user for password
    password = input("Enter your password, or enter exit to cancel: ")

    # Initializes score for password
    totalCombos = 0
    letterCombos = 0
    alphanumericCombos = 0
    symbolCombos = 0

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
    lowercaseCombo = 0
    uppercaseCombo = 0
    digitsCombo = 0
    punctuationCombo = 0
    symbolsCombo = 0
    unidentifiedCombo = 0

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
    if lowercase != 0:
        lowercaseCombo = 26**lowercase
    if uppercase != 0:
        uppercaseCombo = 26**uppercase
    if digits != 0:
        digitsCombo = 10**digits
    if punctuation != 0:
        punctuationCombo = len(punctuationList)**punctuation
    if symbols != 0:
        symbolsCombo = len(symbolList)**symbols
    if unidentified != 0:
        unidentifiedCombo = (95 - 52 - 10 - len(punctuationList) - len(symbolList))**unidentified

    # Calculates password integrity by finding the number of combinations of the password
    totalCombos += lowercaseCombo + uppercaseCombo + digitsCombo + punctuationCombo + symbolsCombo + unidentifiedCombo
    letterCombos += lowercaseCombo + uppercaseCombo
    alphanumericCombos += lowercaseCombo + uppercaseCombo + digitsCombo

    #Checks if length of password is less than 15
    if len(password) < 15:
        print("Your password is less than 15 characters long. This is too short.\n")

    # Checks if the password contains only letters
    if password.isalpha():
        print("Your password contains only letters. This is acceptable.\n")
        print(f"Your password has {letterCombos:,} possible combinations.\n")
        crack_time(letterCombos)
    elif password.isdigit():
        print("Your password contains only digits. This is not good.\n")
        print(f"Your password has {digitsCombo:,} possible combinations.\n")
        crack_time(digitsCombo)
    elif password.isalnum():
        print("Your password contains only alphanumeric characters. This is acceptable.\n")
        print(f"Your password has {alphanumericCombos:,} possible combinations.\n")
        crack_time(alphanumericCombos)
    else:
        print("Your password contains a variety of characters. This is great!\n")
        print(f"Your password has {totalCombos:,} possible combinations.\n")
        crack_time(totalCombos)

    if not password.isdigit() and len(password) >= 15:
        print(f"Your password {password} is acceptable.")
        break


