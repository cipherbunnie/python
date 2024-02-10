# Author: Vam
# Date: 14/01/2024

'''
Assume that a file containing a series of integers is named numbers.txt. 
Write a program that calculates the average of all the numbers stored 
in the file and prints the average to the screen.
Print only the average to the screen, with no formatting. 
The following sample run shows an example.
'''

'''
Function calculate_average(file_path):
    Try:
        Open file at file_path for reading
        Read each line from the file and convert it to an integer
        Calculate the average of the integers
        Print the average
    Except FileNotFoundError:
        Print "File not found."
    Except ValueError:
        Print "Invalid data in the file."

Input file_path
Call calculate_average(file_path)
'''

def calculate_average(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            average = sum(numbers) / len(numbers)
            print(average)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data in the file.")

# Example usage:
file_path = input("Enter the path to the numbers file: ")
calculate_average(file_path)