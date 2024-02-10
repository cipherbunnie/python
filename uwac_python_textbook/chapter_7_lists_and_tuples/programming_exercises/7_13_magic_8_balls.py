# Author: Vam
# Date: 14/01/2024

'''
Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy
that displays a random response to a yes or no question. In the student sample
programs for this book, you will find a text file named
8_ball_responses.txt. 
The file contains 12 responses, such as "I don't
think so", "Yes, of course!", "I'm not sure", and so forth. 

The program should read the responses from the file into a list. 
It should prompt the user to ask a question, then 
display one of the responses, randomly selected from the list.
The program should repeat until the user is ready to quit.
'''

import random

def read_responses():
    with open("8_ball_responses.txt", "r") as file:
        return [line.strip() for line in file]

def get_user_question():
    return input("Ask the Magic 8 Ball a yes or no question: ")

def get_random_response(responses):
    return random.choice(responses)

def main():
    responses = read_responses()

    while True:
        user_question = get_user_question()

        if user_question.lower() == 'quit':
            print("Goodbye!")
            break

        response = get_random_response(responses)
        print(f"Magic 8 Ball says: {response}\n")

if __name__ == "__main__":
    main()
