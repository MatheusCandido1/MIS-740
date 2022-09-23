"""
# Sales History
This application 


* Author: Matheus Carvalho
* Date: 09-23-2022
"""
salesHistory = []
currentAmount = 0.0

print('Please enter the sales amount for each month. Enter -1 when all the sales amounts are entered.')
currentAmount = float(input())

if currentAmount > 0:
  salesHistory.append(currentAmount)


while currentAmount != -1:
  print('Please enter the sales amount (-1 to end):')
  currentAmount = float(input())

  if currentAmount == -1:
    # Call function
    #print('Please enter a target sales amount:')
    #targetValue = float(input())
    print(salesHistory)
    #print('There are X months earning at least 5000.0')
  else: 
    salesHistory.append(currentAmount)
