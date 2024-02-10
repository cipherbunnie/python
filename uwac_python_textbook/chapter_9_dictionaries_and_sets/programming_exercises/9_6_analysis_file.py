# Author: Vam
# Date: 14/01/2024

'''
Write a program that reads the contents of two text files and compares them in
the following ways:
    • It should display a list of all the unique words contained in both files.
    • It should display a list of the words that appear in both files.
    • It should display a list of the words that appear in the first file but not
    the second.
    • It should display a list of the words that appear in the second file but not
    the first.
    • It should display a list of the words that appear in either the first or
    second file, but not both.
Hint: Use set operations to perform these analyses.
'''

def compare_text_files(file1, file2):
    try:
        with open(file1, 'r') as file:
            content1 = set(file.read().lower().split())

        with open(file2, 'r') as file:
            content2 = set(file.read().lower().split())

        # Display a list of all unique words
        all_unique_words = content1.union(content2)
        print("All Unique Words:")
        print(sorted(all_unique_words))

        # Display words that appear in both files
        common_words = content1.intersection(content2)
        print("\nWords Appearing in Both Files:")
        print(sorted(common_words))

        # Display words that appear in the first file but not the second
        unique_to_file1 = content1.difference(content2)
        print("\nWords Appearing Only in File 1:")
        print(sorted(unique_to_file1))

        # Display words that appear in the second file but not the first
        unique_to_file2 = content2.difference(content1)
        print("\nWords Appearing Only in File 2:")
        print(sorted(unique_to_file2))

        # Display words that appear in either file but not both
        symmetric_difference = content1.symmetric_difference(content2)
        print("\nWords Appearing in Either File, But Not Both:")
        print(sorted(symmetric_difference))

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Input filenames
file1_name = 'file1.txt'  # Replace with your first file name
file2_name = 'file2.txt'  # Replace with your second file name

# Compare text files
compare_text_files(file1_name, file2_name)
