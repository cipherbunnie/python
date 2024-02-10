# Author: Vam
# Date: 14/01/2024

'''
In physics, an object that is in motion is said to have kinetic energy. The following formula can be used
to determine a moving object's kinetic energy:
KE = 1/2 * m * v^2
The variables in the formula are as follows: KE is the kinetic energy, m is the object's mass in kilograms,
and v is the object's velocity in meters per second. Write a function named kinetic_energy that accepts
an object's mass (in kilograms) and velocity (in meters per second) as arguments. The function should
return the amount of kinetic energy that the object has. Write a program that asks the user to enter
values for mass and velocity, then calls the kinetic_energy function to get the object's kinetic energy.
'''

'''
Function to calculate kinetic energy
kinetic_energy(mass, velocity)
    KE = 0.5 * mass * velocity^2
    Return KE

Function to get valid user input
get_valid_input(prompt)
    while true
        try
            Attempt to convert user input to a float
            If successful, return the valid value
        except ValueError
            If conversion fails, catch the ValueError and display an error message

# Main program
Print "Enter the mass of the object in kilograms: "
Read mass with valid_input function

Print "Enter the velocity of the object in meters per second: "
Read velocity with valid_input function

Call the kinetic_energy function with user-input values

# Display the calculated kinetic energy
Print format"The kinetic energy of the object is: " with result
'''

# Function to calculate kinetic energy
def kinetic_energy(m, v):
    KE = 0.5 * m * v**2
    return KE

# Function to validate user input
def valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main program
print("Enter the mass of the object in kg:")
m = valid_input("")

print("Enter the velocity of the object in m/s:")
v = valid_input("")

# Call the kinetic_energy function with user-input values
result = kinetic_energy(m, v)

# Display the calculated kinetic energy with formatted output
print(f"The kinetic energy of the object is: {result:.2f}")
