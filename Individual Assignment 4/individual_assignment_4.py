"""
# Part Price Checker
Input: 
Output: 
Processing: 
1 - Get the part number from the user
2 - Validate the part number
3 - If the part number is not valid, ask the user to enter again
4 - If the part number is valid, get the price and store it in a dictionary
5 - Ask the user if he wants to check another part
6 - If the user wants to check another part, go to step 1
7 - If the user does not want to check another part, print all the parts and the prices

* Author: Matheus Carvalho
* Date: 10-10-2022
"""
# Create constants to facilitate further updates
VALID_START = ('P','T')
VALID_END = ('M','O')
BASE_PRICE = 85.00
PRICE_FOR_TRUCK_PARTS = 75.00
MULTIPLIER_FOR_PARTS_FROM_EXTERNAL_VENDORS = 3

# Define function to get the price of the part based on the part number
def get_part_price(partNumber):
  partPrice = BASE_PRICE

  if partNumber.startswith('T'):
    partPrice += PRICE_FOR_TRUCK_PARTS
  
  if partNumber.endswith('O'):
    partPrice *= MULTIPLIER_FOR_PARTS_FROM_EXTERNAL_VENDORS

  return int(partPrice)

# Define function to validate the part number size
def validate_part_number_size(partNumber):
  if len(partNumber) == 5:
    return True
  else:
    print('The part number should be 5 digits. \n')
    return False

# Define function to validate the beginning of the part number and the end of the part number
def validate_part_number(partNumber):
  if not partNumber.startswith(VALID_START):
    print('The first character should be either P or T. \n')
    return False
  if not partNumber.endswith(VALID_END):
    print('The last character should be either M or O. \n')
    return False
  else:
    return True

# Define function to validate the middle numbers of the part number
def validate_part_middle_numbers(partNumber):
  if(partNumber[1:4].isdigit()):
    return True
  else:
    print('The second, third, and fourth characters should be an integer. \n')
    return False

# Define function that calls all other functions to validate the part number and return the price
def validate_part(partNumber):
  if validate_part_number_size(partNumber):
    if validate_part_number(partNumber):
      if validate_part_middle_numbers(partNumber):
        return '$' + str(get_part_price(partNumber))

# Define function to print the dictionary with the part number and the price
def print_parts(parts):
  print('All the parts and the prices just checked')
  for part in parts:
    print(part.ljust(10, '.') + str(parts.get(part)).rjust(4))

# Define function to remove all blank spaces from the part number
def format_part(partNumber):
  partNumber = partNumber.replace(" ", "")
  return partNumber
  
# Set the dictionary to store the part number and the price
parts = {}

# Set flag to control the while loop
checkOtherPart = True

while checkOtherPart:

  # Get the part number from the user
  print('Please enter the part number:')
  partNumber = format_part(input().upper())

  # Validate the part number
  partPrice = validate_part(partNumber)
    
  # If the part number is not valid, ask the user to enter a new part number
  while not partPrice:
    print('pleaser enter again: ')
    partNumber = format_part(input().upper())
    partPrice = validate_part(partNumber)

  # If the part number is valid, add the part number and the price to the dictionary
  print('The part ' + partNumber + ' is $' + str(get_part_price(partNumber)))
  parts[partNumber] = validate_part(partNumber)

  # Ask the user if he wants to check another part
  print('Do you have more parts to check? (y/n)')
  checkOtherPart = input().upper()

  # If the user wants to check another part, set the flag to True
  while checkOtherPart != 'Y' and checkOtherPart != 'N':
    print('Do you have more parts to check? (y/n)')
    checkOtherPart = input().upper()

  # If the user does not want to check another part, set the flag to False
  if checkOtherPart == 'N':
    checkOtherPart = False
  # If the user wants to check another part, set the flag to True
  else:
    checkOtherPart = True
# Print the dictionary with the part number and the price
print_parts(parts)