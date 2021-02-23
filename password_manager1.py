#password_manager.py
#create and display passwords for users 
#K.Juneja Feb 22, 2021

name = ""
age = ""
line = "----------------------------------------------------------------------------------------"

password_list = []

user_list = ["khushiej", "LjiDJoR!03"]

def menu(name):
    print(line)
    mode = int(input("""Choose mode by entering a number: \n1.Add passwords \n2.View Passwords \n3.Exit"""))
    return mode

def add_password():
    print(line)
    pass_input = input("Enter a new password: ")
    password_list.append(pass_input)

def display():
    print(line)
    for password in password_list:
        print("{}".format(password))

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
            break
    elif user == "N": 
        age = int(input("What is your age?: "))
        if age < 13:
            print("Sorry you must be over 13 to use password manager")
            exit()
        else: 
            print("Thank you")
        u_username = input("Enter unsername: ")
        u_password = input("Your password must be at least 8 characters long. \nEnter password:").strip()

        print("Your account has been created!")
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

        


    

