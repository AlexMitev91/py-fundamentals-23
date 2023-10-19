import re

def is_valid_password(password):
    if 6 <= len(password) <= 10:
        if re.match("^[a-zA-Z0-9]*$", password):
            if len([c for c in password if c.isdigit()]) >= 2:
                return True
            else:
                print("Password must have at least 2 digits")
        else:
            print("Password must consist only of letters and digits")
    else:
        print("Password must be between 6 and 10 characters")
    return False
    

pwd = input()

if is_valid_password(pwd):
    print("Password is valid")




