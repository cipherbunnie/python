# Author: Vam
# Date: 14/01/2024

'''
In the student sample programs for this book, you will find a text file named
1994 _Weekly_Gas_Averages.txt. 
The file contains the average gas price
for each week in the year 1994. (There are 52 lines in the file.) 
Using matplotlib, write a Python program that reads the contents of the file then
plots the data as either a line graph or a bar chart. Be sure to display
meaningful labels along the X and Y axes, as well as the tick marks.
'''

import matplotlib.pyplot as plt

def read_gas_prices(file_path):
    weeks = []
    prices = []
    with open(file_path, 'r') as file:
        for line in file:
            week, price = line.strip().split(',')
            weeks.append(int(week))
            prices.append(float(price))
    return weeks, prices

def plot_line_graph(weeks, prices):
    plt.plot(weeks, prices, marker='o', linestyle='-')
    plt.title('Weekly Gas Prices in 1994')
    plt.xlabel('Weeks')
    plt.ylabel('Average Gas Price ($)')
    plt.grid(True)
    plt.show()

def plot_bar_chart(weeks, prices):
    plt.bar(weeks, prices, color='blue')
    plt.title('Weekly Gas Prices in 1994')
    plt.xlabel('Weeks')
    plt.ylabel('Average Gas Price ($)')
    plt.show()

def main():
    file_path = '1994_Weekly_Gas_Averages.txt'
    weeks, prices = read_gas_prices(file_path)

    # Uncomment one of the following lines based on your preference
    # plot_line_graph(weeks, prices)
    # plot_bar_chart(weeks, prices)

if __name__ == "__main__":
    main()

# Make sure to have Matplotlib installed. You can install it using:
# pip install matplotlib