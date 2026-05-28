# Introductory message
print("Password guidelines:\n"
      "1. Make your password at least 15 characters long.\n"
      "2. Include special characters and/or numbers.\n\n")

# Asks user for password
password = input("Enter your password, or enter exit to cancel: ")

# Loops until the user decides to exit
while password != "exit":

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
    print("Your password has:\n"
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
    # letterCombos += lowercaseCombo + uppercaseCombo
    # alphanumericCombos += lowercaseCombo + uppercaseCombo + digitsCombo
    # symbolCombos += lowercaseCombo + uppercaseCombo + digitsCombo + punctuationCombo + symbolsCombo + unidentifiedCombo

    # Displays total number of combos
    print(f"Your password has {totalCombos:,} possible combinations.")

    if len(password) < 15:
        print(f"Your password is less than 15 characters long. This is bad.")

    # Calculates amount of time it would take the average computer to guess, assuming 100 billion guesses a second
    timeToGuess = totalCombos / 100000000000

    # Depending on the amount of time, finds the most appropriate unit to display how long the computer would take to
    # guess the password
    if timeToGuess < 60:
        print(f"It would take the average computer {timeToGuess:,.4f} seconds at most to guess your password.\n"
              f"On average, it would take {timeToGuess / 2:,.4f} seconds.")
    elif timeToGuess >= 3154000000:
        print(f"It would take the average computer {timeToGuess / 3154000000:,.4f} centuries at most to guess your "
              f"password.\nOn average, it would take {timeToGuess / 3154000000 / 2:,.4f} centuries.")
    elif timeToGuess >= 315400000:
        print(f"It would take the average computer {timeToGuess / 315400000:,.4f} decades at most to guess your "
              f"password.\nOn average, it would take {timeToGuess / 315400000 / 2:,.4f} decades.")
    elif timeToGuess >= 31540000:
        print(f"It would take the average computer {timeToGuess / 31540000:,.4f} years at most to guess your password."
              f"\nOn average, it would take {timeToGuess / 31540000 / 2:,.4f} years.")
    elif timeToGuess >= 2628000:
        print(f"It would take the average computer {timeToGuess / 2628000:,.4f} months at most to guess your password."
              f"\nOn average, it would take {timeToGuess / 2628000 / 2:,.4f} months.")
    elif timeToGuess >= 604800:
        print(f"It would take the average computer {timeToGuess / 604800:,.4f} weeks at most to guess your password.\n"
              f"On average, it would take {timeToGuess / 604800 / 2:,.4f} weeks.")
    elif timeToGuess >= 86400:
        print(f"It would take the average computer {timeToGuess / 86400:,.4f} days at most to guess your password\n"
              f"On average, it would take {timeToGuess / 86400 / 2:,.4f} days.")
    elif timeToGuess >= 3600:
        print(f"It would take the average computer {timeToGuess / 3600:,.4f} hours at most to guess your password\n"
              f"On average, it would take {timeToGuess / 3600 / 2:,.4f} hours.")
    elif timeToGuess >= 60:
        print(f"It would take the average computer {timeToGuess / 60:,.4f} minutes at most to guess your password\n"
              f"On average, it would take {timeToGuess / 60 / 2:,.4f} minutes.")

    password = input("Enter your password, or enter exit to cancel: ")

