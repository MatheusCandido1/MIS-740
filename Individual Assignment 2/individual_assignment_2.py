"""
# Phone Bill Calculator Application
This application calculates the phone bill of the customers
Input: Data usage and Account year
Output: Calls and texts charges, data charges and total charges
Processing: 
1 - Get user input
2 - Validate user input
3 - Check the account's year is greater or equal the differentiation year to define the charging rate
4 - Check if the data usage charge exceeded the maximum data charge amount
5 - Calculate the total amount by adding the data charges to the text and phone charges
6 - Show the texts and calls, data and total charges to the user

* Author: Matheus Carvalho
* Date: 09-14-2022
"""
# Define constants to facilitate further updates
UNLIMITED_CALLS_AND_TEXTS_CHARGE = 9.99
OLD_CUSTOMER_RATE = 9.50
NEW_CUSTOMER_RATE = 11.30
MAXIMUM_DATA_CHARGE = 30.00
DIFFERENTIATION_YEAR = 2020


# Set function to format floats and integers to Currency Format
def formatToCurrency(value):
  return '$' + str(format(value,'.2f'))

# Print initial message
print('The purpose of the program is to calculate the cell phone bill for customers of a cell phone company')

# Get the user's data usage
print('Please enter the data usage last month in GB:')
dataUsage = float(input())

# Get the user's account's year
print('Please enter the year the account is opend:')
accountYear = int(input())

# Validate if the inputs are valid 
if dataUsage < 0 or accountYear <= 0:
  print('Invalid input, please try again!')
  exit()

# Check if the user is an old or a new customer and apply the correct rate
if accountYear >= DIFFERENTIATION_YEAR:
  dataUsageSubtotal = dataUsage * NEW_CUSTOMER_RATE
else:
  dataUsageSubtotal = dataUsage * OLD_CUSTOMER_RATE

# Check if the data usage is above the limit to correct the charge
if dataUsageSubtotal > MAXIMUM_DATA_CHARGE:
  dataUsageSubtotal = MAXIMUM_DATA_CHARGE

# Sum the data usage with the default value for calls and texts
total = dataUsageSubtotal + UNLIMITED_CALLS_AND_TEXTS_CHARGE;

# Print all results
print('Calls and Texts: ' + formatToCurrency(UNLIMITED_CALLS_AND_TEXTS_CHARGE))
print('Data: ' + formatToCurrency(dataUsageSubtotal))
print('Total: ' + formatToCurrency(total))