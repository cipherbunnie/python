# Author: Vam
# Date: 14/01/2024

'''
Write a program that reads the contents of a text file. The program should
create a dictionary in which the keys are the individual words found in the file
and the values are the number of times each word appears. For example, if the
word "the" appears 128 times, the dictionary would contain an element with
"the' as the key and 128 as the value. The program should either display the
frequency of each word or create a second file containing a list of each word
and its frequency.
'''

import string

def count_word_frequencies(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # Convert to lowercase for case-insensitivity
            translator = str.maketrans("", "", string.punctuation)  # Remove punctuation
            content = content.translate(translator)
            words = content.split()

        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        print("Word Frequencies:")
        for word, frequency in word_freq.items():
            print(f"{word}: {frequency}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Input filename
input_file_name = 'your_text_file.txt'  # Replace with your text file name

# Display word frequencies
count_word_frequencies(input_file_name)


