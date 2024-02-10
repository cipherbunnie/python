# Author: Vam
# Date: 14/01/2024

'''
In a program, write a function that accepts two arguments; a list, and a number n. 
Assume that the list contains numbers. 
The function should display all the numbers in the list that are greater than the number n. 
Write a program that generates a list containing 1000 random numbers between 1 and 1000. 
The user should be asked to enter a number between a and 1000.
Instead of displaying all the numbers greater than the number entered, they should be written to a file.
'''

'''
function generate_random_numbers():
    Initialize an empty list random_numbers
    Loop 1000 times:
        random_number = generate a random number between 1 and 1000
        Add the random number to the list
    Return the list of random numbers

function write_to_file with numbers, threshold
    Open "output.txt" file for writing   
    for each number in numbers:
        Check if the number is greater than the threshold
            Write the number to the file
    Close the file
    
Function to get valid user input
get_valid_input(prompt)
    while true
        try
            Attempt to convert user input to an integer
            Check if user input between 1 and 1000
                Return the valid value
            Else print error message
        except ValueError
            If conversion fails, catch the ValueError and print an error message

Generate a list of random numbers: numbers_list
Ask the user to enter a number between 1 and 1000 using valid_input function
Filter and write numbers greater than the user-entered number to a file
Inform the user that the process is complete
'''

import random

def generate_random_numbers():
    lst = []
    for _ in range(1000):
        number = random.randint(1, 1000)
        lst.append(number)
    return lst

def write_to_file(lst, n):
    with open("output.txt", "w") as file:
        for i in lst:
            if i > n:
                file.write(f"{i}\n")

def valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 1000:
                return user_input
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Generate a list of random numbers
lst = generate_random_numbers()

# Ask the user to enter a number between 1 and 1000
n = valid_input("Enter a number between 1 and 1000: ")

# Filter and write numbers greater than the user-entered number to a file
write_to_file(lst, n)

# Inform the user that the process is complete
print("Numbers greater than the entered value have been written to 'output.txt'.")
