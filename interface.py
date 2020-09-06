#!/usr/bin/env python3.6
from passlock import User, Credentials

def create_new_user(username, password):
    '''
    Function to create an instance of a user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Function that save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing users
    """
    return User.display_user()

def login_user(username, password):
    """
    function that enables existing users to login.
    """
  
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account, userName, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()

def display_accounts_details():
    """
    Function that displays saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from the credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds Credentials of an account by account name
    """
    return Credentials.find_credential(account)

def check_credendtials(account):
    """
    Function that checks if Credentials exists with an account name and return a boolean
    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password

def copy_password(account):
    """
    A function that allows users to copy password using pyperclip.
    """
    return Credentials.copy_password(account)

def main():
    print('''
Hi! Welcome to Passwords
Use the following commands to navigate the app.
1. 'ca' ---->  Create an Account  
2. 'li' ---->  Have an Account 
        ''')
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        username = input("Username: ")
        while True:
            print(" 't' --> to type your own pasword \n 'g' --> to generate a random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 't':
                password = input("Enter Password:")
                break
            elif password_Choice == 'g':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
                save_user(create_new_user(username, password))
                print(f"Hi {username}, Your account has been created succesfully!)

    elif short_code == "li":
        username = input("Username: ")
        print('\n')
        password = input("Password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hi {username}, Welcome Back To Passwords")  
            print('\n')
    while True:
        print('''
Use the following commands to navigate the app:
1. 'c' - Create a new credential
2. 'f' - Find a credential 
3. 'd' - Display Credentials 
4. 'del' - Delete credential
5. 'g' - Generate A random password 
6. 'x' - Exit the application''')
        short_code = input().lower().strip()
        if short_code == "c":
            print("Create New Credential")
            print("Account name:")
            account = input().lower()
            print("Account username")
            userName = input()
            while True:
                print(" 't' --> To type your own password or g --> To generate a random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 't':
                    password = input("Enter a Password\n")
                    break
                elif password_Choice == 'g':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
                    save_credentials(create_new_credential(account, userName, password))
                    print('\n')
                    print(f'''
Credentials for: {account} 
UserName: {userName} 
Password:{password} 

Created Succesfully!''')
                    print('\n')
        elif short_code == "d":
            if display_accounts_details():
                print("Here's your list of acoounts: ")
                for account in display_accounts_details():
                    print(f'''
Account:{account.account} 
User Name:{username} 
Password:{password}''')
            else:
                print("we haven't registered any credentials with this account")
        elif short_code == "f":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "del":
            print("Enter the account name of the Credentials you want to delete: ")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                search_credential.delete_credentials()
                print('\n')
                print(f"{search_credential.account} credentials have been deleted.")
                print('\n')
            else:
                print("That credential is unavailable for deletion.")

        elif short_code == 'g':

            password = generate_Password()
            print(f" {password} is now the password for your account")
        elif short_code == 'x':
            print("Thank you for choosing passwords!")
            break
        else:
            print("Please Enter a Valid Code to Proceed")
    else:
        print("Please Enter a Valid Code to Proceed")

if __name__ == '__main__':
    main()