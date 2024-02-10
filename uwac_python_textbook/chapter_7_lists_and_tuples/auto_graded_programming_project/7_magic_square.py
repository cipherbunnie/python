# Author: Vam
# Date: 14/01/2024

'''
A Magic Square is a grid with 3 rows and 3 columns with the following properties:
    The grid contains every number from 1 to 9.
    The sum of each row, each column, and each diagonal all add up to the same number.
This is an example of a Magic Square:
4 9 2
3 5 7
8 1 6 

In Python, you can simulate a 3x3 grid using a two-dimensional list. 
For example, the list corresponding to the grid above would be: 
[[4, 9, 2], [3, 5, 7], [8, 1, 6]]
Write the definition of a function named is_magic_square that 
accepts a two-dimensional list as an argument and 
returns either True or False to indicate whether the list is a Magic Square. 
(Submit only the function definition, not a complete program.)
'''

'''
'''

def is_magic_square(grid):
    # Check if all numbers from 1 to 9 are present in the grid
    numbers = set(range(1, 10))
    flat_grid = [num for row in grid for num in row]

    if set(flat_grid) != numbers:
        return False

    # Calculate the sum of the first row for reference
    target_sum = sum(grid[0])

    # Check rows
    for row in grid:
        if sum(row) != target_sum:
            return False

    # Check columns
    for col in range(3):
        if sum(row[col] for row in grid) != target_sum:
            return False

    # Check diagonals
    if sum(grid[i][i] for i in range(3)) != target_sum or sum(grid[i][2 - i] for i in range(3)) != target_sum:
        return False

    return True

# Example usage:
magic_square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
result = is_magic_square(magic_square)
print(result)  # This should print True for the given example
