# Author: Vam
# Date: 14/01/2024

'''
In a program, write a function that accepts two arguments: a list, and a number
n. Assume that the list contains numbers. The function should display all of the
numbers in the list that are greater than the number n.
'''

def display_numbers_greater_than(lst, n):
    # Filter numbers greater than n
    result = [num for num in lst if num > n]

    # Display the filtered numbers
    if result:
        print("Numbers greater than", n, "in the list:", result)
    else:
        print("No numbers greater than", n, "in the list.")

# Example usage
numbers_list = [10, 25, 5, 30, 15, 8, 40]
threshold_number = 20

# Call the function with the example list and threshold number
display_numbers_greater_than(numbers_list, threshold_number)
