"""
# Reward Points Calculation

"""
GROCERY_RATE = 10
FOOD_RATE = 5
OTHER_RATE = 20

import pandas as pd
import numpy as np

def calculate_points(category, value):
  if category == 'grocery':
    total = value / GROCERY_RATE
  elif category == 'food':
    total = value / FOOD_RATE
  elif category == 'other':
    total = value / OTHER_RATE
  return total
   

# read the csv file to read the data
dataUtah = pd.read_csv('customer_spending_UT.csv');
dataNevada = pd.read_csv('customer_spending_NV.csv');

utahArray = np.array([{'grocery': dataUtah['grocery'], 'food': dataUtah['food'], 'other': dataUtah['other']}])
nevadaArray = np.array([{'grocery': dataNevada['grocery'], 'food': dataNevada['food'], 'other': dataNevada['other']}])

utahCustomersSpendingRecords = len(nevadaArray[0]['grocery'])
nevadaCustomersSpendingRecords = len(utahArray[0]['grocery'])

totalSpendingRecords = utahCustomersSpendingRecords + nevadaCustomersSpendingRecords

print('There are ' + str(nevadaCustomersSpendingRecords) + ' records for Nevada customers.')
print('There are ' + str(utahCustomersSpendingRecords) + ' records for Utah customers. \n')

totalSpentOnGroceriesArray = np.concatenate([nevadaArray[0]['grocery'], utahArray[0]['grocery']])
totalSpentOnFoodArray = np.concatenate([nevadaArray[0]['food'], utahArray[0]['food']])
totalSpentOOtherArray = np.concatenate([nevadaArray[0]['other'], utahArray[0]['other']])
totalPointsPerCustomer = []

for i in range(totalSpendingRecords):
  totalPointsPerCustomer.append(calculate_points('grocery', totalSpentOnGroceriesArray[i]) + calculate_points('food', totalSpentOnFoodArray[i]) + calculate_points('other', totalSpentOOtherArray[i]))

totalPointsPerCustomerArray = np.array(totalPointsPerCustomer)

meanOfPoints = round(totalPointsPerCustomerArray.mean(),2)
stdOfPoints = round(totalPointsPerCustomerArray.std(),2)
medianOfPoints =  round(np.median(totalPointsPerCustomerArray),2)

print('The mean of points earned is: '.ljust(55, ' ') + str(format(meanOfPoints, '.2f')))
print('The standard deviation of the of points earnded is: '.ljust(55, ' ') + str( format(stdOfPoints, '.2f')))
print('The median of points earnded is: '.ljust(55, ' ') + str( format(medianOfPoints, '.2f')) + '\n')

planitumCustomers = (totalPointsPerCustomerArray >= 700)
goldCustomers = (totalPointsPerCustomerArray >= 650) & (totalPointsPerCustomerArray < 700)
siilverCustomers = (totalPointsPerCustomerArray >= 600) & (totalPointsPerCustomerArray < 650)

print('Platinum customers: '.ljust(25, ' ') + str(planitumCustomers.sum()).rjust(5, ' '))
print('Gold customers: '.ljust(25, ' ') + str(goldCustomers.sum()).rjust(5, ' '))
print('Silver customers: '.ljust(25, ' ') + str(siilverCustomers.sum()).rjust(5, ' '))