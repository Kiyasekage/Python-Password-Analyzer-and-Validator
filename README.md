# Python-Password-Analyzer-and-Validator
*Description

This Python program analyzes and validates a user's password based on basic security rules.
The program asks the user to enter a username and password. It checks whether the password satisfies several requirements such as minimum length, character diversity, and whether the password is different from the username.
During the validation process, the program also analyzes the password and collects all lowercase letters, uppercase letters, and digits found in it. If the password meets the criteria, the program confirms it and displays the detected characters. The user has up to three attempts to enter a valid password.
This project demonstrates basic Python concepts such as loops, conditionals, list operations, and string method usage while introducing simple password validation logic.

*Password Criteria
Password length must be greater than 8 characters
Must contain lowercase letters
Must contain uppercase letters
Must contain digits
Must not be the same as the username

*Example Output
Welcome to checking your password!

Criteria:
1. >8 characters
2. Must contain lowercase, uppercase, and digits
3. Password must not be the same with username

Username: Alex
Password: Alex12345

Hi Alex, your password has been confirmed
Lowercase = ['l', 'e', 'x']
Uppercase = ['A']
Digit = ['1', '2', '3', '4', '5']

*Technologies Used
Python 3
Built-in string methods (islower(), isupper(), isdigit())
