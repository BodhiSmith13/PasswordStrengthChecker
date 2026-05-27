# Introductory message
print("Password guidelines:\n"
      "1. Make your password at least 15 characters long.\n"
      "2. Include special characters and/or numbers.\n\n")

# Asks user for password
password = input("Enter your password: ")

# Initializes score for password
passwordIntegrity = 0

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

print("Your password has:\n"
      f"{lowercase} lowercase letters\n"
      f"{uppercase} uppercase letters\n"
      f"{digits} digits\n"
      f"{punctuation} punctuation\n"
      f"{symbols} symbols\n"
      f"{unidentified} unidentified characters\n")

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
passwordIntegrity += lowercaseCombo + uppercaseCombo + digitsCombo + punctuationCombo + symbolsCombo

print(f"Your password has {passwordIntegrity} possible combinations.")

