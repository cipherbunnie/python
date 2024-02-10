# Author: Vam
# Date: 14/01/2024

'''
Design a program that asks the user to enter 
a store's sales for each day of the week. 
The amounts should be stored in a list. 
Use a loop to calculate the total
sales for the week and display the result.
'''

'''
1. Create a list to store the sales for each day of the week.
2. Initialize a variable to store the total sales.
3. Use a loop to iterate through each day of the week.
    a. Ask the user to enter the sales for the current day.
    b. Add the entered sales to the list.
    c. Add the entered sales to the total sales.
4. Display the total sales for the week.
'''

def calculate_total_sales(sales):
    total_sales = sum(sales)
    return total_sales

def main():
    # Create a list to store sales for each day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_sales = []

    # Use a loop to get sales for each day
    for day in days_of_week:
        sales = float(input(f"Enter sales for {day}: "))
        weekly_sales.append(sales)

    # Calculate total sales
    total_sales = calculate_total_sales(weekly_sales)

    # Display the total sales
    print(f"\nTotal sales for the week: ${total_sales:.2f}")

if __name__ == "__main__":
    main()
