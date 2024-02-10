# Author: Vam
# Date: 14/01/2024

'''
Assume a variable named t has been assigned a tuple 
whose elements are numbers. 
Write some statements that use a while loop to 
count the number of times the first element of 
the tuple appears in the rest of the tuple, 
and assign that number to a variable named repeats. 
Thus, if the tuple contains (1,6,5,7,1,3,4,1), 
then repeats would be assigned the value 2 because 
after the first "1" there are two more "1"s.
'''

'''
Assign a tuple to the variable t.
Initialize a variable named repeats to 0.
Initialize a variable named target to the first element of the tuple.
Initialize a variable named index to 1.
While index is less than the length of the tuple:
   If the element at index in the tuple is equal to target:
      Increment repeats by 1.
   Increment index by 1.
Display the value of repeats.

'''

# Given a tuple named t
t = (1, 6, 5, 7, 1, 3, 4, 1)
repeats = 0
i = 1  # Start from the second element since we're comparing with the first

while i < len(t):
    if t[i] == t[0]:
        repeats += 1
    i += 1

# The variable 'repeats' now contains the count of the first element's occurrences in the rest of the tuple
print("Number of repeats:", repeats)
