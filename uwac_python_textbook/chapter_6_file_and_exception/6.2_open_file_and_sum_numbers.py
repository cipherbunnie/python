# Author: Vam
# Date: 14/01/2024

'''
A file named numbers.txt contains an unknown number of lines, each consisting of a single integer. 
Write some code that opens the file, computes the sum of all the integers it contains, 
and stores the sum in a variable name sum. Don't forget to close the file.
'''

'''
Initialize the variable to store the sum total_sum = 0
Open the file for reading "numbers.txt"

For loop through each line in the file
    Convert the line content to an integer
    Add the number to the total sum

Close the file
Print the calculated sum
'''

total_sum = 0

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        total_sum += number

print("The sum of all integers in numbers.txt is:", total_sum)
