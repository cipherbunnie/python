# Author: Vam
# Date: 14/01/2024

'''
Design a program that lets the user enter 
the total rainfall for each of 12 months
into a list. 
The program should calculate and 
display the total rainfall for the year, 
the average monthly rainfall, 
the months with the highest and lowest amounts.
'''

'''
Function enterRainfall():
    rainfallList = empty list
    for i from 1 to 12:
        rainfall = input "Enter rainfall for month " + i + ": "
        add rainfall to rainfallList
    return rainfallList

Function calculateTotal(rainfallList):
    total = sum of all elements in rainfallList
    return total

Function calculateAverage(rainfallList):
    average = calculateTotal(rainfallList) / 12
    return average

Function findMaxMinMonths(rainfallList):
    maxMonth = month with highest rainfall in rainfallList
    minMonth = month with lowest rainfall in rainfallList
    return maxMonth, minMonth

Function displayResults(total, average, maxMonth, minMonth):
    print "Total rainfall for the year:", total
    print "Average monthly rainfall:", average
    print "Month with the highest rainfall:", maxMonth
    print "Month with the lowest rainfall:", minMonth

Function main():
    rainfallList = enterRainfall()
    total = calculateTotal(rainfallList)
    average = calculateAverage(rainfallList)
    maxMonth, minMonth = findMaxMinMonths(rainfallList)
    displayResults(total, average, maxMonth, minMonth)

Call main()
'''

def enter_rainfall():
    rainfall_list = []
    for i in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {i}: "))
        rainfall_list.append(rainfall)
    return rainfall_list

def calculate_total(rainfall_list):
    total = sum(rainfall_list)
    return total

def calculate_average(rainfall_list):
    average = sum(rainfall_list) / len(rainfall_list)
    return average

def find_max_min_months(rainfall_list):
    max_month = rainfall_list.index(max(rainfall_list)) + 1
    min_month = rainfall_list.index(min(rainfall_list)) + 1
    return max_month, min_month

def display_results(total, average, max_month, min_month):
    print(f"Total rainfall for the year: {total:.2f}")
    print(f"Average monthly rainfall: {average:.2f}")
    print(f"Month with the highest rainfall: {max_month:.2f}")
    print(f"Month with the lowest rainfall: {min_month:.2f}")

def main():
    rainfall_list = enter_rainfall()
    total = calculate_total(rainfall_list)
    average = calculate_average(rainfall_list)
    max_month, min_month = find_max_min_months(rainfall_list)
    display_results(total, average, max_month, min_month)

if __name__ == "__main__":
    main()
