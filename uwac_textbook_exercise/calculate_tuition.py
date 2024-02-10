# Author: Vam
# Date: 14/01/2024

'''
At one college, the tuition for a full-time student is $32,000 per trimester. 
It has been announced that the tuition will increase by 3 percent each year for the next 5 years. 
Write a program with a loop that displays the projected semester tuition amount for the next 5 years.
'''

'''
This program calculate tuition with 3% increasing each year.

# Initialize variables
tuition = 32000
years = 5
increase_percentage = 3

# Loop for each year
for year in range 1 to years:

    # Update tuition for the current year = tuition + tuition increase for the current year
    tuition = tuition + (tuition * (increase_percentage / 100))
    
    # Display the projected tuition for the current year
    Print format"Year: Projected Semester Tuition - $" with tuition
end loop
'''

# Initial tuition
tuition = 32000

# Number of years
years = 5

# Annual increase percentage
increase_percentage = 3

# Loop to calculate and display tuition for the next 5 years
for year in range(1, years + 1):
    # Calculate the tuition for the current year
    tuition = tuition + (tuition * increase_percentage / 100)
    
    # Display the projected tuition for the current year
    print(f"Year {year}: Projected Semester Tuition - ${tuition:.2f}")

