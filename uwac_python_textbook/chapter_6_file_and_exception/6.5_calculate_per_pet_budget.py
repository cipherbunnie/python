# Author: Vam
# Date: 14/01/2024

'''
Two variables, num_dogs and num_cats, hold the number of dogs and cats 
that have registered for a pet daycare. 
The budget variable holds the number of dollars 
that have been allocated to the daycare for the year.
Write code that displays the per-pet budget (dollar spent per pet), 
rounded to two decimal places. 
If a division by zero error takes place, just print out the word "unavailable".
'''

'''
Function calculate_per_pet_budget(num_dogs, num_cats, budget):
    Try:
        per_pet_budget = budget / (num_dogs + num_cats)
        Return round(per_pet_budget, 2)
    Except ZeroDivisionError:
        Return "unavailable"

Input num_dogs
Input num_cats
Input budget

Result = calculate_per_pet_budget(num_dogs, num_cats, budget)
Output "The per-pet budget is: ", Result
'''

def calculate_per_pet_budget(num_dogs, num_cats, budget):
    try:
        per_pet_budget = budget / (num_dogs + num_cats)
        return round(per_pet_budget, 2)
    except ZeroDivisionError:
        return "unavailable"

# Example usage:
num_dogs = int(input("Enter the number of dogs: "))
num_cats = int(input("Enter the number of cats: "))
budget = float(input("Enter the budget for the daycare: "))

result = calculate_per_pet_budget(num_dogs, num_cats, budget)

print(f"The per-pet budget is: {result}")
