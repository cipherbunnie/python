# Author: Vam
# Date: 14/01/2024

'''
Given:
    a variable named incompletes that refers to a list of student ids, and
    a variable named student_id that has already been assigned a value
Write some code that counts the number of times the value of student_id 
appears in the incompletes list, and assigns this value to number_of_incompletes. 
You may use, if you wish, an additional variable, k.
You may use only k, incompletes, student_id, and number_of_incompletes in your code.
'''

'''
# Input: List of student IDs (incompletes), Target student ID (student_id)
incompletes = [/* Your list of student IDs */]
student_id = /* Your target student ID */

# Initialize variables
number_of_incompletes = 0

# Count the number of occurrences
for each id in incompletes:
    if id is equal to student_id:
        number_of_incompletes = number_of_incompletes + 1

# Output: Number of occurrences
Display "Number of occurrences:", number_of_incompletes
'''

# Input: List of student IDs (incompletes), Target student ID (student_id)
incompletes = []
student_id = 123

# Initialize variables
number_of_incompletes = 0

# Count the number of occurrences
for id in incompletes:
    if id == student_id:
        number_of_incompletes += 1

# Output: Number of occurrences
print("Number of occurrences:", number_of_incompletes)
