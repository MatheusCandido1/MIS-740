"""
# Sales History
The application allows the user to enter a series of sales numbers, until the user enters -1.
The program then asks the user to enter a benchmark number and shows the number of months
earning at least that amount.
Input: Sales amount for each month and target sales amount (benchmark number)
Output: Number of months earning at least amount
Processing:
1 - Get the user input for sale amount for one month
2 - Check if value is valid for starting the program
3 - Check if the amount for the month is -1, if it's not, save the month amount in a list
4 - Repeat the step 3 until the user enters -1
5 - Once the amount for the month is -1, get the user input for benchmark value
6 - Validate the benchmark value
7 - Call the function that goes through the list and return how many values in the list are greater or equal than the target value
8 - Show how many months had earning at least the target value

* Author: Matheus Carvalho
* Date: 09-23-2022
"""
# Create empty list for the sales history
salesHistory = []

"""
Define function the receives the target value as parameter and goes through the list, counts how many values
are greater or equal the target value and return the counter
"""
def get_number_of_months_and_earning_by_value(benchmarkValue):
  counter = 0
  for sale in salesHistory:
    if(sale >= benchmarkValue):
      counter += 1
  return counter

# Get the sales amount for the first month
print('Please enter the sales amount for each month. Enter -1 when all the sales amounts are entered.')
salesAmount = float(input())

# Validate if the sales amount is valid. If not, ask the user to input the value again
while salesAmount <= 0:
  print('Since you have not entered any amount, sales amount cannot be zero or negative, try again')
  print('Please enter the sales amount for each month. Enter -1 when all the sales amounts are entered.')
  salesAmount = float(input())

# If the user input is valid, insert the value into the list
salesHistory.append(salesAmount)

# Enter the loop to allow the user to enter data for the other months
while salesAmount != -1:
  # Get the sales amount for the month
  print('Please enter the sales amount (-1 to end):')
  salesAmount = float(input())

  # If the value entered by user is different than -1, it means that the value is a sales representation
  if salesAmount != -1:
    # Insert the entered value by the user to the sales history list
    salesHistory.append(salesAmount)
    
  # Check if the input is equal to -1 (means that the user wants to end the program)
  else: 
    # Get the benchmark value  
    print('Please enter a target sales amount:')
    benchmarkValue = float(input())

    # Validate the benchmark value
    while benchmarkValue <= 0:
      print('Target value cannot be zero or negative, try again:')
      print('Please enter a target sales amount:')
      benchmarkValue = float(input())

    # Store the number of months that matched the benchmark values returned from the function
    numberOfMonths = get_number_of_months_and_earning_by_value(benchmarkValue)

    # Print how many months had earning at least the target value
    print('There are ' + str(numberOfMonths) +  ' months earning at least ' + str(format(benchmarkValue,'.1f')))
