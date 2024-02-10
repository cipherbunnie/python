# Author: Vam
# Date: 14/01/2024

'''
Write a program that keeps names and email addresses in a dictionary as key-
value pairs. The program should display a menu that lets the user look up a
person's email address, add a new name and email address, change an existing
email address, and delete an existing name and email address. 

The program should pickle the dictionary and save it to a file when the user exits the
program. Each time the program starts, it should retrieve the dictionary from
the file and unpickle it.

When testing this program, use fake names and email addresses
'''
# pickle reminds me about cucumber pickle tho :)

import pickle

def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def display_menu():
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing name and email address")
    print("5. Exit")

def main():
    filename = 'email_data.pkl'
    email_dict = load_data(filename)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name to look up: ")
            if name in email_dict:
                print(f"Email address: {email_dict[name]}")
            else:
                print("Name not found.")

        elif choice == '2':
            name = input("Enter a new name: ")
            email = input("Enter the email address: ")
            email_dict[name] = email
            print("Name and email address added.")

        elif choice == '3':
            name = input("Enter the name to update: ")
            if name in email_dict:
                email = input("Enter the new email address: ")
                email_dict[name] = email
                print("Email address updated.")
            else:
                print("Name not found.")

        elif choice == '4':
            name = input("Enter the name to delete: ")
            if name in email_dict:
                del email_dict[name]
                print("Name and email address deleted.")
            else:
                print("Name not found.")

        elif choice == '5':
            save_data(email_dict, filename)
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
