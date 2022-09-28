"""
# Fine Calculator for Overdue Books
This application calculates the fine for overdue books in the library used by the patrons.
The application will validate every input from the user and will calculate fines for multiple
books, returning in the end the total fine for the patron.
Input: Number of books and number of days overdue (for each book)
Output: Total fine based on the days overdue
Processing: 
1 - Get the total number of books checked out from user
2 - Validate the total number of books
3 - Get the number of days overdue from each book
4 - Validate the number of days overdue
5 - Calculate the fine based on the days overdue
6 - Acumulate the fines from each book returned with delays
7 - Display the total fine of the patron
8 - Ask the user if the application should run again

* Author: Matheus Carvalho
* Date: 09-28-2022
"""
# Define constants to facilitate further updates
REGULAR_FINE_RATE = 0.10
ADDITIONAL_FINE_RATE = 0.20
MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE = 7

# Define function to format floats and integers to Currency Format
def formatToCurrency(value):
  return '$' + str(format(value,'.2f'))

# Define function to calculate the regular fine 
def get_regular_fine(days):
    return (days) * REGULAR_FINE_RATE

# Define function to calculate the additional fine
def get_additional_fine(days):
  return (days - MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE) * ADDITIONAL_FINE_RATE

# Define function to decide whether the patron should pay regular fine or additional fine
def get_fine_by_amount_of_days_overdue(days):
  if days <= MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE:
    return get_regular_fine(days)
  else:
    return get_regular_fine(MAXIMUM_DAYS_TO_GET_REGULAR_FINE_RATE) + get_additional_fine(days)
  
# Set condition to start the application
calculateFine = True

# Validate if should calculate a new fine
while calculateFine:
  # Initiate total fine for the new patron
  totalFine = 0.00

  # Get the number of books checked out from the user
  print('Please enter the number of books checked out:')
  numberOfBooks = int(input())

  # Check if the number of books is valid
  while numberOfBooks < 1:
    print('The number of books checked out should be a positive number.\nPlease enter again:')
    numberOfBooks = int(input())

  # Initiate book counting
  bookNumber = 0

  # Loop through all books 
  while bookNumber < numberOfBooks:
    # Increment book number
    bookNumber += 1

    # Get the number of days overdue of the current book
    print('For book ' + str(bookNumber) + ', please enter the number of days overdue.')
    numberOfDaysOverdue = int(input())

    # Check if current days overdue is valid
    while numberOfDaysOverdue < 0:
      print('The number of days overdue cannot be negative number.\nPlease enter again:')
      numberOfDaysOverdue = int(input())

    # Call the function to get the fine for the current amount of days overdue
    fineByBook = get_fine_by_amount_of_days_overdue(numberOfDaysOverdue)

    # Acummulate the value of the fine from the current book
    totalFine += float(fineByBook)

    # Show the fine of the current book to the user
    print('Book ' + str(bookNumber) + ': ' + str(numberOfDaysOverdue) + ' day(s) overdue, the fine is ' + str(formatToCurrency(fineByBook)))

    #Check if loop is done
    if bookNumber == numberOfBooks:
      # Show the total fine from all books entered by the user
      print('The total fine for the patron is: ' + formatToCurrency(totalFine))

  # Ask if the user wants to calculate the fine to another patron
  print('Calculate the fine for another patron? (Y/y) to continue')
  calculateFineAgain = input()

  # Check if user wants to calculate fine for another patron
  if calculateFineAgain.lower() == 'y':
    # If the user's input is Y or y, the application runs again
    calculateFine = True
  else:
    # IF the user's input is different from Y or y, the application ends
    calculateFine = False