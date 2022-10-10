"""
# Part Price Checker
Input: 
Output: 
Processing: 
1 - Get the total number of books checked out from user

* Author: Matheus Carvalho
* Date: 10-09-2022
"""

VALID_START = ('P','T')
VALID_END = ('M','O')
BASE_PRICE = 85.00
PRICE_FOR_TRUCK_PARTS = 75.00
MULTIPLIER_FOR_PARTS_FROM_EXTERNAL_VENDORS = 3

def get_part_price(partNumber):
  partPrice = BASE_PRICE

  if partNumber.startswith('T'):
    partPrice += PRICE_FOR_TRUCK_PARTS
  
  if partNumber.endswith('O'):
    partPrice *= MULTIPLIER_FOR_PARTS_FROM_EXTERNAL_VENDORS

  return int(partPrice)


def validate_part_number_size(partNumber):
  if len(partNumber) == 5:
    return True
  else:
    print('The part number should be 5 digits. \n')
    return False

def validate_part_number(partNumber):
  if not partNumber.startswith(VALID_START):
    print('The first character should be either P or T. \n')
    return False
  if not partNumber.endswith(VALID_END):
    print('The last character should be either M or O. \n')
    return False
  else:
    return True

def validate_part(partNumber):
  if validate_part_number_size(partNumber):
    if validate_part_number(partNumber):
      return get_part_price(partNumber)

parts = {}

checkOtherPart = True

while checkOtherPart:
  print('Please enter the part number:')
  partNumber = input().upper()

  partPrice = validate_part(partNumber)
    
  while not partPrice:
    print('pleaser enter again: ')
    partNumber = input().upper()
    partPrice = validate_part(partNumber)


  print('The part ' + partNumber + ' is $' + str(get_part_price(partNumber)))
  parts[partNumber] = validate_part(partNumber)

  print('Do you have more parts to check? (y/n)')
  checkOtherPart = input().upper()

  while checkOtherPart != 'Y' and checkOtherPart != 'N':
    print('Do you have more parts to check? (y/n)')
    checkOtherPart = input().upper()

  if checkOtherPart == 'N':
    checkOtherPart = False
  else:
    checkOtherPart = True


print('All the parts and the prices just checked')
for part in parts:
  print(part + '.....$' + str(parts.get(part)))