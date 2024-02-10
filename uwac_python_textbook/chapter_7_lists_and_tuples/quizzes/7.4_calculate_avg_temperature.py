# Author: Vam
# Date: 14/01/2024

'''
Assume the variable temps has been assigned a list that 
contains floating-point values representing temperatures. 
Write code that calculates the average temperature and 
assign it to a variable named avg_temp. 
Besides temps and avg_temp, you may use two other variables -- k and total.
'''

'''
# Input: List of temperatures
temps = [/* Your list of temperatures */]

# Initialize variables
total = 0
k = length of temps
avg_temp = 0

# Calculate total temperature
for each temp in temps:
    total = total + temp

# Calculate average temperature
if k is not 0:
    avg_temp = total / k
else:
    Display "Cannot calculate average for an empty list"

# Output: Average temperature
Display "Average Temperature:", avg_temp
'''

temps = [] 
total = 0
k = len(temps)

for temp in temps:
    total += temp

avg_temp = total / k
