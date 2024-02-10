# Author: Vam
# Date: 14/01/2024

'''
Three variables, x, y, and z, supposedly hold strings of digits, 
suitable for converting to integers. 
Write code that converts these three variables to integers and 
print the sum of these three integers. 

However, if any variable has a value that cannot be converted to an integer, 
display the string "bad value(s) in: " followed by the names of the variables 
that have bad values (separated by spaces, in alphabetically ascending order).

For example, if the values of x, y, and z were respectively 
"3", "9", and "2" then the number 14 would be displayed; 
but if the values were "abc", "15", and "boo" then the output would be:
bad value(s) in: x z
'''

'''
Function convert_and_sum(x, y, z):
    Try:
        x_int = Convert x to integer
        y_int = Convert y to integer
        z_int = Convert z to integer
        result = x_int + y_int + z_int
        Print result
    Except ValueError:
        bad_values = List of variable names with non-integer values
        Print "bad value(s) in: " + Join bad_values in alphabetical order

Input x
Input y
Input z

Call convert_and_sum(x, y, z)
'''

def convert_and_sum(x, y, z):
    try:
        x_int = int(x)
        y_int = int(y)
        z_int = int(z)
        result = x_int + y_int + z_int
        print(result)
    except ValueError:
        bad_values = [var_name for var_name, var_value in [("x", x), ("y", y), ("z", z)] if not var_value.isdigit()]
        print(f"bad value(s) in: {' '.join(sorted(bad_values))}")

# Example usage:
x = input("Enter value for x: ")
y = input("Enter value for y: ")
z = input("Enter value for z: ")

convert_and_sum(x, y, z)
