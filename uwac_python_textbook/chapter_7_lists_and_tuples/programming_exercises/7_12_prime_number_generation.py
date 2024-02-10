# Author: Vam
# Date: 14/01/2024

'''
A positive integer greater than 1 is said to be prime if it has no divisors other
than 1 and itself. A positive integer greater than 1 is composite if it is not prime.
Write a program that asks the user to enter an integer greater than 1, then
displays all of the prime numbers that are less than or equal to the number
entered. The program should work as follows:
    • Once the user has entered a number, the program should populate a list
    with all of the integers from 2 up through the value entered.
    • The program should then use a loop to step through the list. The loop
    should pass each element to a function that displays whether the
    element is a prime number, or a composite number.
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime_status(numbers):
    for num in numbers:
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is a composite number.")

def main():
    try:
        user_input = int(input("Enter an integer greater than 1: "))
        if user_input <= 1:
            print("Please enter an integer greater than 1.")
            return

        numbers_list = list(range(2, user_input + 1))
        display_prime_status(numbers_list)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
