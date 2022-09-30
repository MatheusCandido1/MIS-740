"""
# Fantasy Game
* Author: Matheus Carvalho
* Date: 09-30-2022
"""
def is_not_blank(string):
  return bool(string and not string.isspace())

def get_sum_of_items(inventory):
  total = 0
  for item in inventory:
    total += inventory.get(item)
  
  return total

inventory = {}

print('Please enter the item you just looted: (blank to end)')
item = input()

inventory[item] = 1

while is_not_blank(item):
  print('Please enter the item you just looted: (blank to end)')
  item = input()
  if is_not_blank(item):
    if item in inventory:
      inventory[item] += 1
    else:
      inventory[item] = 1

print('Inventory:')

for item in inventory:
  print(str(inventory.get(item)) + ' ' +  str(item))

print('Total number of items: ' + str(get_sum_of_items(inventory)))