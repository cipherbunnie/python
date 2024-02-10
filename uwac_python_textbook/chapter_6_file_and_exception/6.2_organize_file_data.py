# Author: Vam
# Date: 14/01/2024

'''
A file named data.txt contains an unknown number of lines, each consisting of a single integer.
Write a program that creates the following three files:
    dataplus.txt
    dataminus.txt
    zeros.txt
The program should read each line of the data.txt file and perform the following:
If the line contains a positive number, that number should be written to the 
dataplus.txt file.
If the line contains a negative number, that number should be written to the 
dataminus.txt file.
If the line contains the value 0, do not write the value to a file. 
Instead, keep a count of the number of times 0 is read from the data.txt file.
After all the lines have been read from the data.txt file, 
the program should write the count of zeros to the zeros.txt file.
'''

'''
Open data.txt for reading
Open dataplus.txt for writing
Open dataminus.txt for writing
Initialize count_zeros to 0

For each line in data.txt:
    Read the line as an integer
    If the integer is positive:
        Write the integer to dataplus.txt
    If the integer is negative:
        Write the integer to dataminus.txt
    If the integer is 0:
        Increment count_zeros

Write count_zeros to zeros.txt
Close data.txt, dataplus.txt, dataminus.txt, and zeros.txt
'''

# Open the source file for reading
with open("data.txt", "r") as source_file:
    # Open the destination files for writing
    with open("dataplus.txt", "w") as plus_file, open("dataminus.txt", "w") as minus_file, open("zeros.txt", "w") as zeros_file:
        # Initialize a count for zeros
        zeros_count = 0
        
        # Loop through each line in the source file
        for line in source_file:
            # Convert the line to an integer
            number = int(line)
            
            # Check conditions and write to respective files
            if number > 0:
                plus_file.write(str(number) + "\n")
            elif number < 0:
                minus_file.write(str(number) + "\n")
            else:
                zeros_count += 1
        
        # Write the count of zeros to the zeros.txt file
        zeros_file.write(str(zeros_count))
