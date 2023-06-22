# Author: Dan Treacy
# Date: 13/06/2023
# Version: 1.1.3

# Name: Gelos Enterprises Login Program

import os
import random
import string
import sys
import time

# Global to store account information
accounts = {}


# Main Menu
def main():
    load_accounts()
    while True:
        # Present menu of options to user
        print("Please press the indicated key to make your choice\n")
        print("(L)ogin\n(R)egister\n(V)iew accounts\n(E)xit")
        choice = input("Choose an option: ")
        if choice.lower() == 'l':
            login()
        elif choice.lower() == 'r':
            register()
        elif choice.lower() == 'v':
            view_accounts()
        elif choice.lower() == 'e':
            print("Exiting the program...")
            time.sleep(1)
            print("Peace...")
            time.sleep(1)
            print('Out!')
            break
        else:
            print("Invalid option!")


# Load accounts.txt from disk
def load_accounts():
    if os.path.isfile('accounts.txt'):
        with open('accounts.txt', 'r') as f:
            for line in f.readlines():
                username, password = line.strip().split(' ')
                accounts[username] = password

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check if the entered username and password match an account in the 'accounts' dictionary
    if username in accounts and accounts[username] == password:
        print("\nLogin successful!")
    else:
        print("\nInvalid username or password!")


# Register a new user
def register():
    username = input("Enter a username: ")
    # Check if the username is already taken
    if username in accounts:
        print("Username already exists!")
        return
    password = input("Do you want to (1) enter your password or (2) generate a password? ")
    if password == '1':
        password = input("Enter your password: ")
    else:
        length = input("Enter the password length (default is 8): ")
        if not length:
            length = 8
        else:
            length = int(length)
        chars = input("Choose character types - (1) numbers, (2) symbols, (3) letters, (4) all: ")
        if chars == '1':
            chars = string.digits
        elif chars == '2':
            chars = string.punctuation
        elif chars == '3':
            chars = string.ascii_letters
        else:
            chars = string.ascii_letters + string.digits + string.punctuation
        # Generate a password using the specified character types and length
        password = ''.join(random.choice(chars) for _ in range(length))
        print("Your generated password is: ", password)
    # Add the new account to the 'accounts' dictionary
    accounts[username] = password
    save_accounts()


# Save account information to accounts.txt
def save_accounts():
    with open('accounts.txt', 'a') as f:
        for username, password in accounts.items():
            f.write(f'{username} {password}\n')


# Display all account information to user
def view_accounts():
    print("\nUsernames and passwords:")
    for username, password in accounts.items():
        print(f'{username} {password}')


# Add initial data to accounts.txt if it doesn't exist
def seed_accounts_txt():
    pass


# Program Start
if __name__ == "__main__":
    main()
