# Author: Vam
# Date: 14/01/2024

'''
Write a program that creates a dictionary containing 
course numbers and the room numbers of the rooms where the courses meet. 
The dictionary should have the following key-value pairs:
        Course Number (key)         Room Number (key)
        CS101                       3004
        CS102                       4501
        CS103                       6755
        NT110                       1244
        CM241                       1411
The program should also create a dictionary containing 
course numbers and the names of the instructors that teach each course. 
The dictionary should have the following key-value pairs:
        Course Number (key)         Instructor (value)
        CS101                       Haynes
        CS102                       Alvarado
        CS103                       Rich
        NT110                       Burke
        CM241                       Lee
The program should also create a dictionary containing 
course numbers and the meeting times of each course. 
The dictionary should have the following key-value pairs:
        Course Number (key)         Meeting Time (value)
        CS101                       8:00am
        CS102                       9:00am
        CS103                       10:00am
        NT110                       11:00am
        CM241                       1:00pm
The program should let the user enter a course number, 
and then it should display the course's room number, instructor, and meeting time.
'''

# Dictionary of course numbers and room numbers
room_numbers = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411',
}

# Dictionary of course numbers and instructors
instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee',
}

# Dictionary of course numbers and meeting times
meeting_times = {
    'CS101': '8:00am',
    'CS102': '9:00am',
    'CS103': '10:00am',
    'NT110': '11:00am',
    'CM241': '1:00pm',
}

def display_course_info(course_number):
    room_number = room_numbers.get(course_number, 'Not found')
    instructor = instructors.get(course_number, 'Not found')
    meeting_time = meeting_times.get(course_number, 'Not found')

    print(f"Course Number: {course_number}")
    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")

def main():
    course_number = input("Enter a course number: ")
    display_course_info(course_number)

if __name__ == "__main__":
    main()
