PasswordStrengthChecker is a password creator coded in Python. The purpose of this program is to analyze the strength of inputted passwords in the form of strings and evaluate them based on a grading program.
Passwords are graded based on length, character variety, and whether or not the password is a pass phrase. A pass phrase is a string of words that are easy to remember; so long as the pass phrase is long enough,
it will be secure. The program first analyzes the content of the password, counting the occurrence of each type of character. These types include lowercase and uppercase letters, digits, punctuation, symbols,
and all other non-unicode characters. For each character type found, the number of members in that character set are tallied together. Then, the total number of combinations of that password are found by raising
the size of the character set to the power of the length of the password. The total number of combos is then compared to the computational strength of the average computer. The longest and average amount of time to crack the givenpassword is then calculated. Finally, the password is graded out of 5, with each result being displayed for the user. If the password is a pass phrase, it gets 2 points. If the password is at least 15 characters long, it gets 3 points. If the password has letters, digits, and one other character type, it gets 1 point. If the password gets a score of higher than 3, the password is deemed acceptable and the program ends. Otherwise, the program loops until an acceptable password is inputted. 

To build, open the project folder in PyCharm and install pyenchant via pip. Note that pyenchant also requires a system-level enchant binary. On Windows, download and install the standalone enchant binary from the pyenchant GitHub releases page. On Mac, run brew install enchant. On Linux, run sudo apt install enchant-2. Once both are installed, run the default build configuration in PyCharm.

The guidelines for password collection were sourced from NIST: https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password

Example Output:
```
Do you want debug enabled? Input anything for yes, or press enter to continue.
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

Your password is 4 characters long. This is too short.

Your password is not a passphrase.

Your password contains only digits. This is not good.

Your password has 10,000 possible combinations.

The average computer can make 100 billion attempts a second at cracking your password.
It would take the average computer 0.0000 seconds at most to guess your password.
On average, it would take 0.0000 seconds.

Your password has scored 0 out of 5 possible points.

Your password 1234 is rejected.

Enter your password, or enter exit to cancel: Sharksseekblood

Your password has:
14 lowercase letters
1 uppercase letters
0 digits
0 punctuation
0 symbols
0 unidentified characters

Your password is 15 characters long. This is great!

Your password is a passphrase.

Your password contains only letters. This is acceptable.

Your password has 54,960,434,128,018,667,122,720,768 possible combinations.

The average computer can make 100 billion attempts a second at cracking your password.
It would take the average computer 174,256.2908 centuries at most to guess your password.
On average, it would take 87,128.1454 centuries.

Your password has scored 5 out of 5 possible points.

Your password Sharksseekblood is acceptable.
