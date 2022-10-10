"""
# Fantasy Game
This application works as a simple inventory system for a fantasy game, keeping track of the items and their quantities.
Input: Item name
Output: Inventory list and total number of items
Processing:
1 - Get user input
2 - Validate user input
3 - Get user input for item name
4 - Validate user input for item name
5 - Check if item is already in inventory
6 - If item is already in inventory, ask user to input a new item name
7 - If item is not in inventory, create a new item in inventory
8 - Keep asking the user to input item names until the user inputs 'blank or space'
9 - Show the inventory list and total number of items to the user
* Author: Matheus Carvalho
* Date: 09-30-2022
"""
# Define function to validate if character is not blank nor space
def is_not_blank(string):
  return bool(string and not string.isspace())

# Define function to get sum of items in inventory
def get_sum_of_items(inventory):
  total = 0
  for item in inventory:
    total += inventory.get(item)
  
  return total

# Set inventory dictionary to store the items and their quantities
inventory = {}

# Get user input for the item name
print('Please enter the item you just looted: (blank to end)')
item = input()

# Validate if the item is not blank nor space
if is_not_blank(item):
  inventory[item] = 1

# Loop to get the items and their quantities while the user does not input a blank item
while is_not_blank(item):
  
  # Get user input for the item name
  print('Please enter the item you just looted: (blank to end)')
  item = input()
  # Validate if the item is not blank nor space
  if is_not_blank(item):
    # Check if the item is already in the inventory, if it is, increment the quantity by 1
    if item in inventory:
      inventory[item] += 1
    # If not, add the item to the inventory
    else:
      inventory[item] = 1

# Print the inventory string
print('Inventory:')

# Loop to print the items and their quantities to print the inventory
for item in inventory:
  print(str(inventory.get(item)) + ' ' +  str(item))

# Print the total number of items
print('Total number of items: ' + str(get_sum_of_items(inventory)))