# Author: Vam
# Date: 14/01/2024

'''
If you have downloaded the source code you will find a file in the Chapter 07
folder named popular_names.txt. This file contains a list of the 400 most
popular names given to children born in the United States from the year 2000
through 2009.
Write a program that reads the contents of file into a list. The user should be
able to enter a name and the program will display a message indicating
whether the name was among the most popular.
'''

'''
procedure check_popularity(names_list, user_input)
    if user_input in names_list then
        output(user_input, "was among the most popular names between 2000 and 2009.")
    else
        output(user_input, "was not among the most popular names between 2000 and 2009.")
    end if
end procedure

# Example usage:
# Assume names_list is a list read from the popular_names.txt file
names_list <- [/* contents of the file */]

# Assume user_input is provided by the user
user_input <- input("Enter a name: ")

check_popularity(names_list, user_input)
'''

def check_popularity(names_list, user_input):
    if user_input in names_list:
        print(f"{user_input} was among the most popular names between 2000 and 2009.")
    else:
        print(f"{user_input} was not among the most popular names between 2000 and 2009.")

# Read the list of popular names from the file
file_path = "popular_names.txt"
with open(file_path, "r") as file:
    names_list = [name.strip() for name in file.readlines()]

# Get user input
user_input = input("Enter a name: ")

# Check popularity
check_popularity(names_list, user_input)
