# Author: Vam
# Date: 14/01/2024

'''
If you have downloaded the source code from the Computer Science Portal you
will find a file named charge_accounts. txt in the Chapter 07 folder. 
This file has a list of a company's valid charge account numbers. 
Each account number is a seven-digit number, such as 5658845.

Write a program that reads the contents of the file into a list. 
The program should then ask the user to enter a charge account number.
The program should determine whether the number is 
valid by searching for it in the list. 

If the number is in the list, the program should display a message 
indicating the number is valid. 
If the number is not in the list, the program should display a
message indicating the number is invalid.
'''

'''
# Function to read charge account numbers from file into a list
function read_charge_accounts(filename):
    try:
        open file named filename
        read lines from file into accounts_list
        close file
        return accounts_list
    except FileNotFoundError:
        print("File not found.")
        return empty list

# Function to check if a charge account number is valid
function is_valid_account(account_number, accounts_list):
    if account_number in accounts_list:
        return True
    else:
        return False

# Main program
function main():
    # Read charge account numbers from file
    accounts_file = "charge_accounts.txt"
    charge_accounts = read_charge_accounts(accounts_file)

    if not charge_accounts:
        return  # Exit if unable to read the file

    # Get user input for a charge account number
    user_account = user input as integer

    # Check if the entered account number is valid
    if is_valid_account(user_account, charge_accounts):
        print("The account number is valid.")
    else:
        print("The account number is invalid.")

# Call the main function
if program is executed directly:
    call main()
'''

def read_charge_accounts(filename):
    try:
        with open(filename, 'r') as file:
            accounts_list = [int(line.strip()) for line in file]
        return accounts_list
    except FileNotFoundError:
        print("File not found.")
        return []

def is_valid_account(account_number, accounts_list):
    return account_number in accounts_list

def main():
    # Read charge account numbers from file
    accounts_file = "charge_accounts.txt"
    charge_accounts = read_charge_accounts(accounts_file)

    if not charge_accounts:
        return  # Exit if unable to read the file

    # Get user input for a charge account number
    user_account = int(input("Enter a charge account number: "))

    # Check if the entered account number is valid
    if is_valid_account(user_account, charge_accounts):
        print("The account number is valid.")
    else:
        print("The account number is invalid.")

# Call the main function
if __name__ == "__main__":
    main()
