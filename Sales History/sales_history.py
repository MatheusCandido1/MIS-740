"""
# Sales History
This application 


* Author: Matheus Carvalho
* Date: 09-23-2022
"""
def getNumberOfMonthsAndEarningByValue(salesHistory, targetValue):
  counter = 0
  for sale in salesHistory:
    if(sale >= targetValue):
      counter += 1
  return counter

salesHistory = []
currentAmount = 0.0

print('Please enter the sales amount for each month. Enter -1 when all the sales amounts are entered.')
currentAmount = float(input())

if currentAmount > 0:
  salesHistory.append(currentAmount)
  while currentAmount != -1:
    print('Please enter the sales amount (-1 to end):')
    currentAmount = float(input())

    if currentAmount >= 0:
      salesHistory.append(currentAmount)
    else: 
      print('Please enter a target sales amount:')
      targetValue = float(input())

      while targetValue <= 0:
        print('Target value cannot be negative, try again:')
        print('Please enter a target sales amount:')
        targetValue = float(input())

      numberOfMonths = getNumberOfMonthsAndEarningByValue(salesHistory, targetValue)
      print('There are ' + str(numberOfMonths) +  ' months earning at least $' + str(format(targetValue,'.2f')))
