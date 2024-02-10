# Author: Vam
# Date: 14/01/2024

'''
Assume the file popular_names.txt contains the 400 most popular names 
given to children born in the United States from the year 2000 through 2009. 
The file contains 400 lines, with one name per line.

Write a program that reads the contents of the file into a list. 
The program should display the following string to prompt the user to enter a name:
'Enter a name: '

The program should then display a message indicating whether the name is 
among the most popular. 
If the name is found in the list, the program should display the following message:
'That was a popular name between 2000 and 2009.'

If the name is not found in the list, the program should display the following message:
'That was not a popular name between 2000 and 2009.'

Look carefully at the following sample runs of the program. 
In the first sample run, the user enters a name that is found in the list. 
In the second sample run, the user enters a name that is not found in the list. 
Carefully notice the wording of the messages and the placement of spaces and colons. 
Your program's output must match this.
'''

'''
# Open the file and read names into a list
Open 'popular_names.txt' file
Initialize an empty list named popular_names

For each line in the file:
    Strip leading and trailing whitespaces from the line
    Add the stripped line to the popular_names list

# Prompt the user to enter a name
Display 'Enter a name: '
Read user_input

# Check if the entered name is in the list
If user_input is in popular_names:
    Display 'That was a popular name between 2000 and 2009.'
Else:
    Display 'That was not a popular name between 2000 and 2009.'
'''

# Open the file and read names into a list
with open('popular_names.txt', 'r') as file:
    popular_names = [line.strip() for line in file]

# Prompt the user to enter a name
user_input = input('Enter a name: ')

# Check if the entered name is in the list
if user_input in popular_names:
    print('That was a popular name between 2000 and 2009.')
else:
    print('That was not a popular name between 2000 and 2009.')

