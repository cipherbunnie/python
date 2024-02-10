# Author: Vam
# Date: 14/01/2024

'''
Write a program that creates a dictionary containing the U.S. states as keys, and
their capitals as values. (Use the Internet to get a list of the states and their
capitals.) The program should then randomly quiz the user by displaying the
name of a state and asking the user to enter that state's capital. The program
should keep a count of the number of correct and incorrect responses. (As an
alternative to the U.S. states, the program can use the names of countries and
their capitals.)
'''

import random

def quiz_user(states_and_capitals):
    correct_answers = 0
    incorrect_answers = 0

    # Get a list of states from the dictionary
    states = list(states_and_capitals.keys())

    # Shuffle the order of states for a random quiz
    random.shuffle(states)

    # Quiz the user
    for state in states:
        capital = states_and_capitals[state]
        user_input = input(f"What is the capital of {state}? ").strip()

        if user_input.lower() == capital.lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Sorry, the correct answer is {capital}.\n")
            incorrect_answers += 1

    # Display quiz results
    print("\nQuiz Results:")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")

# Dictionary of U.S. states and capitals
us_states_and_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    # Add more states and capitals as needed
}

# Start the quiz
quiz_user(us_states_and_capitals)
