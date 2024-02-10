# Author: Vam
# Date: 14/01/2024

'''
Write a program that uses a dictionary to assign "codes" to each letter of the
alphabet. For example:
codes = { 'A': 'g', 'a': '9', 'B': '@', 'b': '#', etc... }

Using this example, the letter A would be assigned the symbol %, the letter a
would be assigned the number 9, the letter B would be assigned the symbol @
and so forth.

The program should open a specified text file, read its contents, then use the
dictionary to write an encrypted version of the file's contents to a second file.
Each character in the second file should contain the code for the corresponding
character in the first file.

Write a second program that opens an encrypted file and displays its decrypted
contents on the screen.
'''

# ENCRYPT

def encrypt_file(input_filename, output_filename, codes):
    try:
        with open(input_filename, 'r') as input_file:
            original_text = input_file.read()

        encrypted_text = ''.join(codes.get(char, char) for char in original_text)

        with open(output_filename, 'w') as output_file:
            output_file.write(encrypted_text)

        print(f"Encryption successful. Encrypted text saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# Example codes
encryption_codes = {'A': 'g', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '$'}

# Input and output filenames
input_file_name = 'input.txt'  # Replace with your input file name
output_file_name = 'encrypted_output.txt'  # Replace with your desired output file name

# Perform encryption
encrypt_file(input_file_name, output_file_name, encryption_codes)


# DECRYPT

def decrypt_file(input_filename, codes):
    try:
        with open(input_filename, 'r') as input_file:
            encrypted_text = input_file.read()

        decrypted_text = ''.join([k for v, k in codes.items() if v == char][0] if char in codes else char for char in encrypted_text)

        print("Decrypted Text:\n", decrypted_text)
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# Example codes (same as in encryption program)
decryption_codes = {'g': 'A', '9': 'a', '@': 'B', '#': 'b', '!': 'C', '$': 'c'}

# Input filename for decryption
input_file_name_decrypt = 'encrypted_output.txt'  # Replace with the filename used for encryption

# Perform decryption
decrypt_file(input_file_name_decrypt, decryption_codes)

