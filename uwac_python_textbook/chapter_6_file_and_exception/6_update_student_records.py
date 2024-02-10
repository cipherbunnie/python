# Author: Vam
# Date: 14/01/2024

'''
A file exists on the disk named students.txt. 
The file contains several records, and each record contains 
two fields: (1) the student's name, 
and (2) the student's score for the final exam. 
Write code that deletes the record containing "John Perz" 
as the student name and changes Julie Milan's score to 100.
'''

'''
Function update_student_records(file_path):
    Try:
        Open file at file_path for reading
        Read all lines from the file

        Open file at file_path for writing
        For each line in lines:
            Split line into name and score
            If name is "John Perz", skip this line (delete the record)
            Else if name is "Julie Milan", write "{name},{100}" to the file
            Else write the line to the file

    Except FileNotFoundError:
        Print "File not found."

Input file_path
Call update_student_records(file_path)
'''

def update_student_records(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                # Split each line into name and score
                name, score = line.strip().split(',')

                # Check if the name is "John Perz" and update the score
                if name == "John Perz":
                    continue  # Skip this record (delete)
                elif name == "Julie Milan":
                    file.write(f"{name},{100}\n")  # Change Julie Milan's score to 100
                else:
                    file.write(line)  # Keep other records unchanged

    except FileNotFoundError:
        print("File not found.")

# Example usage:
file_path = "students.txt"  # Replace with the actual file path if needed
update_student_records(file_path)
