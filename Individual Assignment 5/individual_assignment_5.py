"""
# Course Record
This application work as a course record system. It can add new courses into the file and print the content of the file.
Input: File name that contains the course records, course number, course name, semester the course is taken, number of credits, and grade.
Output: File containig the course record.
Processing:
1 - Get the file name that contains the course record from the user.
2 - Validate the file format.
3 - Validate the file name, if the file doesn't exists, exit the program.
4 - Open the file in read mode.
5 - Get all the course record from the file and store them in a list.
6 - Convert the list to a NumPy array.
7 - Close the file.
8 - Print the content of the file.
9 - Ask the user if he wants to add a new course.
10 - If the user wants to add a new course, get the course number, course name, semester the course is taken, number of credits, and grade from the user.
11 - Validate the number of credits.
12 - Format the course number, course name, semester the course is taken, number of credits, and grade.
13 - Open the file in append mode.
14 - Write the new course record to the file.
15 - Close the file.
16 - Ask the user if he wants to record another course.
17 - If the user wants to record another course, go to step 10.
18 - If the user does not want to record another course, finish the program.
* Author: Matheus Carvalho
* Date: 10-18-2022
"""
#Import OS to use the path
import os

#Import NumPy to use the array
import numpy as np

# Define function to format course number
def format_course_number(courseNumber):
   # Get the last 3 digits of the course number (ex: 700/740/760)
    code = courseNumber[-3:]

    # Get the original course number and remove the last 3 digits, then we get the course number without the code (ex: MIS/CSEC) and remove all unnecessary spaces
    initials = courseNumber.replace(code, '').replace(' ', '')

    # Concatenate the initials and the code
    formattedCourseNumber = initials.upper() + ' ' + code

    # Return the course number with the code and the initials
    return formattedCourseNumber

# Define function to print the content of the file
def print_file_content(courses):
    # Loop through the array 
    for course in courses:
      # Split the array by comma
      currentCourse = course.split(',')
      # Print the course number, course name, semester the course is taken, number of credits, and grade justifying the text to the left
      print(currentCourse[0].ljust(12, ' ') + currentCourse[1].ljust(35, ' ') + currentCourse[2].ljust(16, ' ') + currentCourse[3].ljust(4, ' ') + currentCourse[4].ljust(4, ' '))

# Ask the user for the file name
print('Please enter the name of a text file with the extension of .txt or .csv:')
fileName = input()

# Validate the file format
while not fileName.endswith('.txt') and not fileName.endswith('.csv'):
    print('Please enter the name of a text file with the extension of .txt or .csv:')
    fileName = input()

# Validate if the file exists
if not os.path.exists(fileName):
  print('The file does not exist')
  # Exit the program if the file does not exist
  exit()

# Open the file in read mode
courseFile = open(fileName, 'r')

# Read all the lines from the file
courseList = courseFile.read().splitlines()
# Convert the list to a NumPy array
courseArray = np.array(courseList)
# Close the file
courseFile.close()

# Call the function to print the content of the file
print_file_content(courseArray)

# Ask the user if he wants to add a new course
print('Would you like to add a new course to the file? (Y/N)')
addNewCourse = input()

# Validate the user input
while addNewCourse.upper() != 'Y' and addNewCourse.upper() != 'N':
  print('Would you like to add a new course to the file? (Y/N)')
  addNewCourse = input()

userInteractedWithFile = False
# Loop while the user wants to add a new course
while addNewCourse.upper() == 'Y':
  # Ask the user for the course number
  print('Please enter the course number:')
  courseNumber = input()
  # Ask the user for the course name
  print('Please enter the course name:')
  courseName = input()
  # Ask the user for the semester the course is taken
  print('Please enter the semester the course is taken:')
  courseSemester = input()
  # Ask the user for the number of credits
  print('Please enter the number of credits:')
  courseCredits = input()
  
  # Validate the number of credits
  while not courseCredits.isnumeric():
    print('The course credits must be a number!')
    print('Please enter the number of credits:')
    courseCredits = input()

  # Ask the user for the grade
  print('Please enter the grade received:')
  courseGrade = input()

  # format the course number, course name, semester the course is taken, number of credits, and grade to insert in the file
  newCourse = f'{format_course_number(courseNumber)},{courseName.title()},{courseSemester.title()},{courseCredits},{courseGrade.upper()}\n'
  # Open the file in append mode
  courseFile = open(fileName, 'a')
  # Write the new course record to the file
  courseFile.write(newCourse)
  # Close the file
  courseFile.close()

  userInteractedWithFile = True

  # Ask the user if he wants to record another course
  print('Would you like to add another course new course record to the file? (Y/N)')
  addNewCourse = input()

  # Validate the user input
  while addNewCourse.upper() != 'Y' and addNewCourse.upper() != 'N':
    print('Would you like to add another course new course record to the file? (Y/N)')
    addNewCourse = input()

# If user has made any updates in the file, Print that the file has been saved. Finish the program    
userInteractedWithFile and print('file saved.')
