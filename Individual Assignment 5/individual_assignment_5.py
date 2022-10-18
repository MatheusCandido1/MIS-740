"""
# Course Record
Processing:
1 - Get user input
* Author: Matheus Carvalho
* Date: 10-18-2022
"""
import os
import numpy as np

def print_file_content(courseList):
    for course in courseList:
        print(course)

path = os.path.join(os.path.dirname(__file__))

print('Please enter the name of a text file with the extension of .txt or .csv:')
fileName = input()

while not fileName.endswith('.txt') and not fileName.endswith('.csv'):
    print('Please enter the name of a text file with the extension of .txt or .csv:')
    fileName = input()


fullPath = path + '\\' + fileName

print(fullPath)
if not os.path.exists(fullPath):
  print('The file does not exist')
  exit()

courseFile = open(fullPath, 'r')

courseList = courseFile.read().splitlines()
courseArray = np.array(courseList)

courseFile.close()

print_file_content(courseArray)

print('Would you like to add a new course to the file? (Y/N)')
addNewCourse = input()

while addNewCourse.upper() != 'Y' and addNewCourse.upper() != 'N':
  print('Would you like to add a new course to the file? (Y/N)')
  addNewCourse = input()


while addNewCourse.upper() == 'Y':
  print('Please enter the course number:')
  courseNumber = input()
  print('Please enter the course name:')
  courseName = input()
  print('Please enter the semester the course is taken:')
  courseSemester = input()
  print('Please enter the number of credits:')
  courseCredits = input()
  print('Please enter the grade received:')
  courseGrade = input()
  newCourse = f'{courseNumber.upper()},{courseName.title()},{courseSemester.title()},{courseCredits},{courseGrade.upper()}\n'
  courseFile = open(fullPath, 'a')
  courseFile.write(newCourse)
  courseFile.close()

  print('Would you like to add another course new course record to the file? (Y/N)')
  addNewCourse = input()

  while addNewCourse.upper() != 'Y' and addNewCourse.upper() != 'N':
    print('Would you like to add another course new course record to the file? (Y/N)')
    addNewCourse = input()
    
print('file saved.')

