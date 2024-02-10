# Author: Vam
# Date: 14/01/2024

'''
Assume that a file named golf.txt exists in the current working directory. 
The file contains the names of golfers and their final scores in a tournament. 
The file is structured so there is a line with the golfer's name 
followed by their score on the next line. 
Here is an example of the file's contents:
Luka
72
Mateo
76
Marissa
74
Rohan
78
Write a program that reads the golf.txt file and 
prints each golfer's name and score as shown in the following sample run. 
Notice the placement of spaces, colons, and blank lines. 
Your program's output must match this.
'''

'''
Function print_golf_scores(file_path):
    Try:
        Open file at file_path for reading
        Read all lines from the file
        For each even-indexed line in lines:
            Extract name by stripping the line
            Extract score from the next odd-indexed line
            Print "{name}: {score}"
    Except FileNotFoundError:
        Print "File not found."

Input file_path
Call print_golf_scores(file_path)
'''

def print_golf_scores(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                name = lines[i].strip()
                score = lines[i + 1].strip()
                print(f"{name}: {score}")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
file_path = "golf.txt"  # Replace with the actual file path if needed
print_golf_scores(file_path)
