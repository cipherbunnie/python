# Author: Vam
# Date: 14/01/2024

'''
Design a program that asks the user to enter a series of 20 numbers. 
The program should store the numbers in a list then 
display the following data:
    The lowest number in the list
    The highest number in the list
    The total of the numbers in the list
    The average of the numbers in the list
'''

'''
# Function to calculate and display statistics
function display_statistics(numbers)
    if not numbers
        print "The list is empty."
        return

    lowest = minimum of numbers
    highest = maximum of numbers
    total = sum of numbers
    average = total / length of numbers

    print lowest number 
    print highest number
    print total of the numbers
    print average of the numbers

# Main program
function main
    numbers = empty list

    # Get user input for 20 numbers
    for i in range 20
        input_number = user input as float
        add input_number to numbers

    # Display statistics
    display_statistics function

# Call the main function
if program is executed directly
    call main function
'''

# Function to calculate and display statistics
def display_statistics(numbers):
    # Check if the list is empty
    if not numbers:
        print("The list is empty.")
        return

    # Calculate statistics
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Display results
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average:.2f}")

# Main program
def main():
    # Get user input for 20 numbers
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(20)]

    # Display statistics
    display_statistics(numbers)

# Call the main function
if __name__ == "__main__":
    main()
