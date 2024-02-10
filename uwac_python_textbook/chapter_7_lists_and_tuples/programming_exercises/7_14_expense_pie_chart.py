# Author: Vam
# Date: 14/01/2024

'''
Create a text file that contains your expenses for last month in the following
categories:
    • Rent
    • Gas
    • Food
    • Clothing
    • Car payment
    • Misc
Write a Python program that reads the data from the file and uses
matplot lib to plot a pie chart showing how you spend your money.
'''

import matplotlib.pyplot as plt

def read_expenses(file_path):
    expenses = {}
    with open(file_path, 'r') as file:
        for line in file:
            category, amount = line.strip().split()
            expenses[category] = float(amount)
    return expenses

def plot_pie_chart(expenses):
    labels = expenses.keys()
    values = expenses.values()

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Monthly Expenses Breakdown')
    plt.show()

def main():
    file_path = 'expenses.txt'
    expenses = read_expenses(file_path)
    plot_pie_chart(expenses)

if __name__ == "__main__":
    main()

# Make sure to have Matplotlib installed. You can install it using:
# pip install matplotlib