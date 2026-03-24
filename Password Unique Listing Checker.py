print("Welcome to checking your password!")
print("Criteria :  \n1. >8 characters\n2. Must contain lowercase, uppercase, and digits\n3. password must not be the same with username ")
name = input("Username: ")
attempts = 3
for i in range(attempts):
    password = input("Password: ")
    has_lower = []
    has_upper = []
    has_number = []
    for char in password:
        if char.islower():
            has_lower.append(char)
        elif char.isupper():
            has_upper.append(char)
        elif char.isdigit():
            has_number.append(char)
    if(len(password)>8 and has_lower and has_upper and has_number and password != name):
        print(f"Hi {name}, your password has been confirmed")
        print(f"Lowercase = {has_lower}\nUppercase = {has_upper}\nDigit = {has_number}")
        break
    else:
        remaining = attempts -i- 1
        print(f"Dear {name}, your password does not meet our criteria")
        if remaining>0:
            print(f"You have {remaining} attempt(s)")
        else:
            print("You have failed to create a valid password")
        