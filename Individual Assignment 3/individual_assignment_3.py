"""
# Fine Calculator for Overdue Books

Input: 
Output: 
Processing: 
1 - Get user input

* Author: Matheus Carvalho
* Date: 09-28-2022
"""
REGULAR_FINE_RATE = 0.10
ADDITIONAL_FINE_RATE = 0.20
MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE = 7

def formatToCurrency(value):
  return '$' + str(format(value,'.2f'))
  
def get_regular_fine(days):
    return (days) * REGULAR_FINE_RATE

def get_additional_fine(days):
  return (days - 7) * ADDITIONAL_FINE_RATE

def get_fine_by_amount_of_days_overdue(days):
  if days <= MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE:
    return get_regular_fine(days)
  else:
    return get_regular_fine(MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE) + get_additional_fine(days)
  

calculateFine = True

while calculateFine:
  totalFine = 0.00
  print('Please enter the number of books checked out:')
  numberOfBooks = int(input())

  while numberOfBooks < 1:
    print('The number of books checked out should be a positive number.\nPlease enter again:')
    numberOfBooks = int(input())

  bookNumber = 0

  while bookNumber < numberOfBooks:
    bookNumber += 1
    print('For book ' + str(bookNumber) + ', please enter the number of days overdue.')
    numberOfDaysOverdue = int(input())

    while numberOfDaysOverdue < 0:
      print('The number of days overdue cannot be negative number.\nPlease enter again:')
      numberOfDaysOverdue = int(input())
    #Check value for this one
    fineByBook = get_fine_by_amount_of_days_overdue(numberOfDaysOverdue)
    totalFine += float(fineByBook)

    print('Book ' + str(bookNumber) + ': ' + str(numberOfDaysOverdue) + ' day(s) overdue, the fine is ' + str(formatToCurrency(fineByBook)))
    if bookNumber == numberOfBooks:
      print('The total fine for the patron is: ' + formatToCurrency(totalFine))

  print('Calculate the fine for another patron? (Y/y) to continue')
  calculateFineAgain = input()

  if calculateFineAgain.lower() == 'y':
    calculateFine = True
  else:
    calculateFine = False