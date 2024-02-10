# Author: Vam
# Date: 14/01/2024

'''
The local driver's license office has asked you to create an application that
grades the written portion of the driver's license exam. The exam has 20
multiple-choice questions.

Your program should store these correct answers in a list. The program should
read the student's answers for each of the 20 questions from a text file and store
the answers in another list. (Create your own text file to test the application.)
After the student's answers have been read from the file, the program should
display a message indicating whether the student passed or failed the exam. (A
student must correctly answer 15 of the 20 questions to pass the exam.) It
should then display the total number of correctly answered questions, the total
number of incorrectly answered questions, and a list showing the question
numbers of the incorrectly answered questions.
'''

'''
procedure grade_exam(correct_answers, student_answers)
    num_correct = 0
    incorrect_questions = []

    for i = 1 to length(correct_answers) do
        if student_answers[i] == correct_answers[i] then
            num_correct = num_correct + 1
        else
            append i to incorrect_questions
        end if
    end for

    passed = num_correct >= 15

    output("Results:")
    output("Total Correct Answers:", num_correct)
    output("Total Incorrect Answers:", length(correct_answers) - num_correct)
    output("Incorrect Question Numbers:", incorrect_questions)

    if passed then
        output("Congratulations! You passed the exam.")
    else
        output("Sorry, you did not pass the exam.")
    end if
end procedure
'''

def grade_exam(correct_answers, student_answers):
    num_correct = 0
    incorrect_questions = []
    
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            num_correct += 1
        else:
            incorrect_questions.append(i + 1)

    passed = num_correct >= 15

    print("Results:")
    print("Total Correct Answers:", num_correct)
    print("Total Incorrect Answers:", len(correct_answers) - num_correct)
    print("Incorrect Question Numbers:", incorrect_questions)

    if passed:
        print("Congratulations! You passed the exam.")
    else:
        print("Sorry, you did not pass the exam.")

# Example usage:
correct_answers = ['C', 'A', 'D', 'B', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
# Assume student_answers is a list read from a file or provided by the user
student_answers = ['C', 'A', 'D', 'B', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'A', 'A']

grade_exam(correct_answers, student_answers)
