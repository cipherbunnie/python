# Author: Vam
# Date: 14/01/2024

'''
Assume my_list is a list of integer values. 
Write a list comprehension statement that creates a second list named gt_ten. 
The gt_ten list should contain all the values of my_list that are greater than 10.
For example, if my_list contains the following values:
[1, 12, 2, 20, 3, 15, 4]
The gt_ten list should contain these values:
[12, 20, 15]
'''

# Assuming my_list is a list of integer values
my_list = [1, 12, 2, 20, 3, 15, 4]

# List comprehension to create a second list named gt_ten
gt_ten = [x for x in my_list if x > 10]

# Display the original and gt_ten lists
print("Original List:", my_list)
print("Greater Than Ten List:", gt_ten)
