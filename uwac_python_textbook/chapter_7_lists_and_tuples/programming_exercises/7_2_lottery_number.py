# Author: Vam
# Date: 14/01/2024

'''
Design a program that generates a seven-digit lottery number. 
The program should generate seven random numbers, 
each in the range of O through 9, and
assign each number to a list element. 
(Random numbers were discussed in Chapter 5.) 
Then write another loop that displays the contents of the list.
'''

'''
Function generateLotteryNumber():
    lotteryNumbers = empty list
    for i from 1 to 7:
        num = random integer between 0 and 9
        add num to lotteryNumbers
    return lotteryNumbers

Function displayLotteryNumber(numbers):
    print "Lottery Number:"
    for num in numbers:
        print num, end=" "
    print newline

Function main():
    lotteryNumbers = generateLotteryNumber()
    displayLotteryNumber(lotteryNumbers)

Call main()
'''

import random

def generate_lottery_number():
    # Generate seven random numbers in the range 0 through 9
    lottery_numbers = [random.randint(0, 9) for _ in range(7)]
    return lottery_numbers

def display_lottery_number(numbers):
    # Display the contents of the list
    print("Lottery Number:")
    for num in numbers:
        print(num, end=" ")
    print()

def main():
    # Generate a seven-digit lottery number
    lottery_numbers = generate_lottery_number()

    # Display the generated lottery number
    display_lottery_number(lottery_numbers)

if __name__ == "__main__":
    main()
