# Author: Vam
# Date: 14/01/2024

'''
If you have downloaded the source code you will find a file named
USPopulation.txt in the Chapter 07 folder. The file contains the midyear
population of the United States, in thousands, during the years 1950 through
1990. The first line in the file contains the population for 1950, the second line
contains the population for 1951, and so forth.

Write a program that reads the file's contents into a list. The program should
display the following data:
    The average annual change in population during the time period
    The year with the greatest increase in population during the time period
    The rear with the smallest increase in during the time period.
'''

def calculate_average_change(population_list):
    total_change = 0
    for i in range(1, len(population_list)):
        change = population_list[i] - population_list[i - 1]
        total_change += change

    average_change = total_change / (len(population_list) - 1)
    return average_change

def find_max_min_increase(population_list):
    max_increase = max(population_list[i] - population_list[i - 1] for i in range(1, len(population_list)))
    min_increase = min(population_list[i] - population_list[i - 1] for i in range(1, len(population_list)))

    max_year = population_list.index(max_increase) + 1950
    min_year = population_list.index(min_increase) + 1950

    return max_year, min_year

# Read the population data from the file
file_path = "USPopulation.txt"
with open(file_path, "r") as file:
    population_list = [int(line.strip()) for line in file.readlines()]

# Calculate average annual change
average_change = calculate_average_change(population_list)
print(f"Average annual change in population: {average_change:.2f} thousands")

# Find years with the greatest and smallest increase in population
max_increase_year, min_increase_year = find_max_min_increase(population_list)
print(f"Year with the greatest increase in population: {max_increase_year}")
print(f"Year with the smallest increase in population: {min_increase_year}")
