import re
#Stage 1
def validate_email(email):
    if '@' in email and '@' != email[-1] and '@' != email[0] and email.count('@') == 1 and len(email) > 1:
        first_part = email.split('@')[0]
        second_part = email.split('@')[1]

        if '.' in second_part and '.' != second_part[0] and len(second_part) > 1 and '.' != second_part[-1]:
            return True
        else:
            return False
    else:
        return False

def validate_password(password):
    is_special = True
    is_digit = True
    is_upper = True
    is_lower = True
    is_alpha = True

    #Ganesh@gmail.com
    # pass@123

    if len(password) > 5 and len(password) < 16:
        for i in password:
            if i.isnumeric():
                is_digit = True

            if i.isalpha():
                is_alpha = True

            if i.islower():
                is_lower = True

            if i.isupper():
                is_upper = True

        if is_special and is_digit and is_lower and is_upper and is_alpha:
            return True
        else:
            return False

#Stage 2 

def validate_credentials(email, password):
    return validate_email(email) and validate_password(password)


def store_password(email, password):
    with open('emailpass.txt', 'r') as f:
        f.write(f'{email} {password}\n')


def get_credentials(filename='emailpass.txt'):
    credentials = []
    with open(filename, 'r') as f:
        f.seek(0)
        lines = f.readlines()
        for i in lines:
            i_id = i.split()[0]
            i_pass = i.split()[1]
            credentials.append([i_id, i_pass])


    return credentials


def login(email, password):
    credentials = get_credentials()

    for i in credentials:
        if email == i[0]:
            if password == i[1]:
                return True

    return False

def registration():
    email = input("Enter Email Id: ")
    while not validate_email(email):
        email = input("Invalid email address. Please enter a valid email: ")
    password = input("Enter a password (The password must contain atlease one special character "
                     ", one digit, one uppercase, one lowercase and should be 5 to 16 characters long): ")
    while not validate_password(password):
        password = input("Invalid password. Please enter a valid password: ")

    with open('emailpass.txt', 'a') as file:
        file.write(email + " " + password + "\n")

    print("Account created successfully")

def forget_pass(creds, ind):
    print("\nPress 1 to know your old password.")
    print("press 2 to change password")

    inp = int(input())

    if inp == 1:
        print("\nOld password: ", creds[ind].split(" ")[1])
    elif inp == 2:
        password = input("\nEnter new Password: ")
        while not validate_password(password):
            password = input("Invalid password. Please enter a valid password: ")

        creds[ind] = creds[ind].split(" ")[0] +" "+password
        with open('emailpass.txt', 'w+') as file:
            for cred in creds[:-1]:
                file.write(cred+"\n")

        print("Password Changed Successfully")
    else:
        print("Invalid input")



def login():
    email = input("Enter Email Id: ")
    password = input("Enter password: ")
    file = 0
    try:
        file =  open('emailpass.txt', 'r+')
    except:
        print("file does not exist. Please register some entries.")
        return

    creds = file.read().split("\n")
    for ind, cred in enumerate(creds[:-1]):
        id, pas = cred.split(" ")
        if id == email:
            if pas == password:
                print("Welcome!Back")
                print("Your Login Details are matching.")
                return
            else:
                print("The password you provided is incorrect.")
                inp = input("Forgot password (n/y): ")
                if inp.upper() == 'Y':
                    forget_pass(creds, ind)
                return
    print("The email does not exist.")
    inp = input("Do you want to register? (y/n): ")
    if inp.upper() == 'Y':
        print(end='\n')
        registration()
    file.close()

if __name__ == '__main__':
    print("Press 1 for registration.")
    print("Press 2 for login.")
    input_1 = int(input())
    print(end="\n")

    if input_1 == 1:
        registration()
    elif input_1 == 2:
        login()
    else:
        print("Invalid input")


    #Ganesh@gmail.com
    # pass@123
    #incase Password Wrong Means Please enter Caps "Y" For update 
    #incase want to register new  means please enter Caps "Y" For update 