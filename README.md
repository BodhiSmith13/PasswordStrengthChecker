PasswordStrengthChecker is a password creator coded in Python. The purpose of this program is to analyze the strength of inputted passwords in the form of strings and evaluate them based on a grading program.
Passwords are graded based on length, character variety, and whether or not the password is a pass phrase. A pass phrase is a string of words that are easy to remember; so long as the pass phrase is long enough,
it will be secure. The program first analyzes the content of the password, counting the occurrence of each type of character. These types include lowercase and uppercase letters, digits, punctuation, symbols,
and all other non-unicode characters. For each character type found, the number of members in that character set are tallied together. Then, the total number of combinations of that password are found by multiplying
the size of the character set by the length of the password. The total number of combos is then compared to the computational strength of the average computer. The longest and average amount of time to crack the given
password is then calculated. Finally, the password is graded, with each result being displayed for the user. If the password gets a score of 3 or higher, the password is deemed acceptable and the program ends. Otherwise,
the program loops until an acceptable password is inputted. 

To build, open the project folder in PyCharm and run the default build configuration. 

The guidelines for password collection were sourced from NIST: https://www.nist.gov/cybersecurity-and-privacy/how-do-i-create-good-password

Example Output:
```
Do you want debug enabled? Input anything for yes, or press enter to continue.1234
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

Charset size: 10

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

Charset size: 52

Your password is 15 characters long. This is great!

Words found in password:
Sh, Shark, Sharks, ha, hark, harks, a, ar, ark, arks, ks, ss, see, seek, eek, kb, bl, blood, lo, loo, oo, od
Words found in password that begin with the first character of the password:
Sh, Shark, Sharks
Starting with Sh
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Appending a
Sha matches Sha
Looking at ar, word 8 in the word list
Appending ar
Shar matches Shar
Looking at ark, word 9 in the word list
Appending ark
Shark matches Shark
Looking at arks, word 10 in the word list
Appending arks
Sharks matches Sharks
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Sha, Shar, Shark, Sharks
Starting with Sha
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list

Starting with Shar
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Appending ks
Sharks matches Sharks
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Sharks
Starting with Sharks
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Appending see
Sharkssee matches Sharkssee
Looking at seek, word 14 in the word list
Appending seek
Sharksseek matches Sharksseek
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Sharkssee, Sharksseek
Starting with Sharkssee
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Appending kb
Sharksseekb matches Sharksseekb
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Sharksseekb
Starting with Sharksseekb
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Appending lo
Sharksseekblo matches Sharksseekblo
Looking at loo, word 20 in the word list
Appending loo
Sharksseekbloo matches Sharksseekbloo
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Sharksseekblo, Sharksseekbloo
Starting with Sharksseekblo
Looking at Sh, word 1 in the word list
Looking at Shark, word 2 in the word list
Looking at Sharks, word 3 in the word list
Looking at ha, word 4 in the word list
Looking at hark, word 5 in the word list
Looking at harks, word 6 in the word list
Looking at a, word 7 in the word list
Looking at ar, word 8 in the word list
Looking at ark, word 9 in the word list
Looking at arks, word 10 in the word list
Looking at ks, word 11 in the word list
Looking at ss, word 12 in the word list
Looking at see, word 13 in the word list
Looking at seek, word 14 in the word list
Looking at eek, word 15 in the word list
Looking at kb, word 16 in the word list
Looking at bl, word 17 in the word list
Looking at blood, word 18 in the word list
Looking at lo, word 19 in the word list
Looking at loo, word 20 in the word list
Looking at oo, word 21 in the word list
Looking at od, word 22 in the word list
Appending od
Sharksseekblood matches Sharksseekblood
Sharksseekblood
Found a phrase that matches the inputted password

Your password is a passphrase.

Your password contains only letters. This is acceptable.

Your password has 54,960,434,128,018,667,122,720,768 possible combinations.

The average computer can make 100 billion attempts a second at cracking your password.
It would take the average computer 174,256.2908 centuries at most to guess your password.
On average, it would take 87,128.1454 centuries.

Your password has scored 5 out of 5 possible points.

Your password Sharksseekblood is acceptable.
