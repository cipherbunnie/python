# Author: Vam
# Date: 14/01/2024

'''
Write a program that reads the contents of a text file. The program should
create a dictionary in which the key-value pairs are described as follows:
Key. The keys are the individual words found in the file.
Values. Each value is a list that contains the line numbers in the file
where the word (the key) is found.
For example, suppose the word "robot" is found in lines 7, 18, 94, and 138. The
dictionary would contain an element in which the key was the string "robot"
and the value was a list containing the numbers 7, 18, 94, and 138.
Once the dictionary is built, the program should create another text file, known
as a word index, listing the contents of the dictionary. The word index file
should contain an alphabetical listing of the words that are stored as keys in the
dictionary, along with the line numbers where the words appear in the original
file.
'''

def create_word_index(input_filename, output_filename):
    word_occurrences = {}

    # Read the contents of the text file
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Create the dictionary with word occurrences
    for line_number, line in enumerate(lines, start=1):
        words = line.split()
        for word in words:
            word = word.strip('.,!?()[]{}:;"\'')  # Remove punctuation
            word = word.lower()  # Convert to lowercase
            if word:
                if word not in word_occurrences:
                    word_occurrences[word] = []
                word_occurrences[word].append(line_number)

    # Create the word index file
    with open(output_filename, 'w') as index_file:
        for word in sorted(word_occurrences.keys()):
            line_numbers = word_occurrences[word]
            index_file.write(f"{word}: {', '.join(map(str, line_numbers))}\n")

if __name__ == "__main__":
    input_file = "your_input_file.txt"  # Replace with the actual input file name
    output_file = "your_word_index.txt"  # Replace with the desired output file name

    create_word_index(input_file, output_file)
