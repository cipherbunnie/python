# Author: Vam
# Date: 14/01/2024

'''
Assume a file named my_data.txt already exists and contains an unknown number of lines. 
Each line contains an integer value. Write a program that copies the contents of 
my_data.txt to another file named my_copy.txt. 
Your program should use the with statement to open both files.
Note: The program should not display any screen output. 
It should simply copy the contents of my_data.txt to my_copy.txt.
'''

'''
Open my_data.txt for reading using with statement as file_input
Open my_copy.txt for writing using with statement as file_output

For each line in file_input:
    Write the line to file_output

Close my_data.txt and my_copy.txt
'''

# Open files for reading using with statement 
with open("my_data.txt", "r") as file_input:
    with open("my_copy.txt", "w") as file_output:
        for line in file_input:
            file_output.write(line)
