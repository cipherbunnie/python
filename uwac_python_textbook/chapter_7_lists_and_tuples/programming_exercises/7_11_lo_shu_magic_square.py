# Author: Vam
# Date: 14/01/2024

'''
The Lo Shu Magic Square is a grid with 3 rows and 3 columns,
    The grid contains the numbers 1 through 9 exactly.
    The sum of each row, each column, and each diagonal all add up to the
    same number. 
In a program you can simulate a magic square using a two-dimensional list.
Write a function that accepts a two-dimensional list as an argument and
determines whether the list is a Lo Shu Magic Square. Test the function in a
program.
'''

def is_lo_shu_magic_square(square):
    # Check if the square has 3 rows
    if len(square) != 3:
        return False

    # Check if each row has 3 columns
    if any(len(row) != 3 for row in square):
        return False

    # Check if the numbers 1 through 9 are present exactly once
    numbers = set()
    for row in square:
        for num in row:
            if num < 1 or num > 9 or num in numbers:
                return False
            numbers.add(num)

    # Check the sum of each row, column, and diagonal
    target_sum = sum(square[0])
    # Check rows
    if any(sum(row) != target_sum for row in square):
        return False
    # Check columns
    if any(sum(square[i][j] for i in range(3)) != target_sum for j in range(3)):
        return False
    # Check diagonals
    if sum(square[i][i] for i in range(3)) != target_sum or sum(square[i][2 - i] for i in range(3)) != target_sum:
        return False

    return True

# Example usage
magic_square = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_lo_shu_magic_square(magic_square):
    print("It's a Lo Shu Magic Square")
else:
    print("It's not a Lo Shu Magic Square")
