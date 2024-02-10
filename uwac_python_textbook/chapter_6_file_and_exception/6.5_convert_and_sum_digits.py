# Author: Vam
# Date: 14/01/2024

'''
Two variables, x and y, supposedly hold strings of digits. 
Write code that converts these to integers and assigns a variable 
z the sum of these two integers. 
Make sure that if either x or y has bad data 
(that is, not a string of digits), z will be assigned the value of -1.
'''

'''
Set x as a string holding digits or any invalid data
Set y as a string holding digits or any invalid data

Try:
    Convert x to an integer
    Convert y to an integer
    Set z as the sum of x and y
Except ValueError:
    Set z as -1
'''

def convert_and_sum_digits(x, y):
    try:
        int_x = int(x)
        int_y = int(y)
        z = int_x + int_y
        return z
    except ValueError:
        return -1
    

# Example usage:
x_input = input("Enter the value for x: ")
y_input = input("Enter the value for y: ")

result = convert_and_sum_digits(x_input, y_input)

if result == -1:
    print("Invalid input. Both x and y should be strings of digits.")
else:
    print(f"The sum of {x_input} and {y_input} is: {result}")