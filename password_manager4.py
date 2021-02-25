#password_manager.py
#create and display passwords for users 
#K.Juneja Feb 22, 2021

#initalise variables and lists
name = ""
age = ""
line = "----------------------------------------------------------------------------------------"

password_list = []

user_list = [["bdsc123", "pass1234"]]

#the menu() function asks the user to choose an option
def menu(name):
    print(line)
    mode = int(input("""Choose mode by entering a number: \n1.Add passwords \n2.View Passwords \n3.Exit"""))
    return mode

#the add_password() function enables the user to store a password
def add_password():
    print(line)
    pass_input = input("Enter a new password: ")
    password_list.append(pass_input)

#the display() function enables the user to view the passwords they have saved
def display():
    print(line)
    for password in password_list:
        print("{}".format(password))

#Main routine - run main programme in a loop 
print("Welcome to password manager")

name = input("What is your name?")

print("Hello", name)

while True: 
    user = input("Please enter: \nL to login or N to create an account: ").upper()
    if user == "L":
        u_username = input("Username: ")
        u_password = input("Password: ")
        if u_username and u_password in user_list: 
            print("Welcome", name)
        dbreak
    elif user == "N": 
        age = float(input("What is your age?: "))
        if age < 13:
            print("Sorry you must be over 13 to use password manager")
            exit()
        else: 
            print("Thank you")
        u_username = input("Enter unsername: ")
        while True:
            u_password = input("Your password must be at least 8 characters long, include a capital letter and a number. \nEnter password:").strip()
            if (any(passreqs.isupper() for passreqs in u_password) and any(passreqs.isdigit()for passreqs in u_password) and len(u_password) >= 8):
                user_list.append([u_username, u_password])
                print("Your account has been created!")
            else: 
                print("Your password does not meet the password requirements. It must have at least 8 characters, include a capital letter and a number")
            break
    else:
        print("That was not a valid option, please enter L to login ot N to create an account: ")

while True: 
    chosen_option = menu(name)
    if chosen_option == 1:
        add_password()
    elif chosen_option == 2:
        display()
    elif chosen_option == 3:
        break
    else: 
        print("That was not a valid option, please try again")

print("Goodbye. Thank you for using password manager")