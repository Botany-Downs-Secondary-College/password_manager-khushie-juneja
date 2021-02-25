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
    #asks user to choose L to login to their exisiting account or choose N to sign up to use password manager 
    user = input("Please enter: \nL to login or N to create an account: ").upper()
    if user == "L":
        #asks user to enter username and password stored in user_list
        u_username = input("Username: ")
        u_password = input("Password: ")
        #allows user to login if entered username and password match to user_list
        if u_username and u_password in user_list: 
            print("Welcome", name)
        break
    elif user == "N": 
        #as user must be >13 to create an account, age variable to check requirement
        age = float(input("What is your age?: "))
        if age < 13:
            print("Sorry you must be over 13 to use password manager")
            exit()
        #if age is >13
        else: 
            print("Thank you")
        #asks user to create username
        u_username = input("Create unsername: ")
        while True:
            #asks user to create password with requirements of 8 characters, capital letter and number
            u_password = input("Your password must be at least 8 characters long, include a capital letter and a number. \nCreate password:").strip()
            #checks all password requirements are met
            if (any(passreqs.isupper() for passreqs in u_password) and any(passreqs.isdigit()for passreqs in u_password) and len(u_password) >= 8):
                user_list.append([u_username, u_password])
                print("Your account has been created!")
                break
            else: 
                print("Your password does not meet the password requirements.")
        break    
    else:
        print("That was not a valid option, please enter L to login ot N to create an account: ")
    

while True: 
    chosen_option = menu(name)
    if chosen_option == 1:
        #calls add_password() function if chosen_option is 1
        add_password()
    elif chosen_option == 2:
        #calls display() function if chosen_option is 2
        display()
    elif chosen_option == 3:
        #breaks if chosen_option  is 3
        break
    else: 
        print("That was not a valid option, please try again")

print("Goodbye. Thank you for using password manager")

