# Author: Vam
# Date: 14/01/2024

'''
Write a program that opens a specified text file then 
displays a list of all the unique words found in the file.
Hint: Store each word as an element of a set.
'''

def unique_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        
        # Split the content into words and create a set to store unique words
        words = set(content.split())
        
        print("Unique Words:")
        for word in words:
            print(word)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Input filename
input_file_name = 'your_text_file.txt'  # Replace with your text file name

# Perform unique words extraction
unique_words(input_file_name)
