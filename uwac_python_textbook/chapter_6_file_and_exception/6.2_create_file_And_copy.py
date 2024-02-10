# Author: Vam
# Date: 14/01/2024

'''
A file named data1.txt contains an unknown number of lines, 
each consisting of a single integer. 
Write some code that creates a file named data2.txt 
and copies all the lines of data1.txt to data2.txt.
'''

'''
Open the source file for reading "data1.txt"
Create or open the destination file for writing "data2.txt" 

Loop through each line in the source file
    Write the line to the destination file

Close both files
'''

# Open the source file for reading
with open("data1.txt", "r") as source_file:
    # Open or create the destination file for writing
    with open("data2.txt", "w") as destination_file:
        for line in source_file:
            destination_file.write(line)
