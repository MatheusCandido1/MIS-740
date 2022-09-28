"""
# Fine Calculator for Overdue Books

Input: 
Output: 
Processing: 
1 - Get user input

* Author: Matheus Carvalho
* Date: 09-21-2022
"""
# Define constants to facilitate further updates

print('Please enter the number of books checked out:')
numberOfBooks = int(input())

while numberOfBooks < 1:
  print('The number of books checked out should be a positive number.\nPlease enter again:')

bookNumber = 0

while bookNumber < numberOfBooks:
  bookNumber += 1
  print('For book ' + str(bookNumber) + ' please enter the number of days overdue.')
  int(input())
  #Check value for this one
  print('Book 1: 10 day(s) overdue, the fine is $1.3')

  if bookNumber == numberOfBooks:
    print('Calculate the fine for another patron? (Y/y) to continue')