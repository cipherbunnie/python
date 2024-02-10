# Author: Vam
# Date: 14/01/2024

'''
Write a function named count_vowels that accepts a string as an argument. 
The function should count the number of times each vowel (the letters a, e, i, o, and u) 
appears in the string, and store those counts in a dictionary. 
When the function ends, the dictionary should have exactly 5 elements. 
In each element, the key will be a vowel (lowercase) and the value will be 
the number of times the vowel appears in the string.

For example, if the string argument is 'Now is the time', 
the function will store the following elements in the dictionary:
'a': 0
'e': 2
'i': 2
'o': 1
'u': 0 
The function should return the dictionary.
'''

def count_vowels(input_string):
    # Initialize a dictionary to store vowel counts
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the input string to lowercase for case-insensitive counting
    input_string = input_string.lower()

    # Count the occurrences of each vowel in the string
    for char in input_string:
        if char in vowel_counts:
            vowel_counts[char] += 1

    # Return the dictionary with vowel counts
    return vowel_counts

# Example usage:
input_str = 'Now is the time'
result = count_vowels(input_str)
print(result)
