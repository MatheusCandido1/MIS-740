"""
# Reward Points Calculation
This application calculates the reward points for many customers based on the amount spent in each category. After this calculation, the application prints the mean, standard deviation and median of the points and how many customers in each category.
Input: Files that contains the spending of each customer in each category in the state of Nevada and Utah.
Output: Mean, standard deviation and median of the points and how many customers in each category.
Processing:
1 - Read the files that contains the spending of each customer in each category in the state of Nevada and Utah from the user.
2 - Create numpy arrays for each state
3 - Count the number of customers in each state
4 - Sum the numbers of customers in each state
5 - Print the number of customers in each state
6 - Create numpy array to acumulate all the spending of grocery, food and other
7 - Loop through the numpy arrays of categories and calculate the points by customers
8 - Calculate the mean, standard deviation and median of the points
9 - Print the mean, standard deviation and median of the points
10 - Create masks to filter the customers by points
11 - Print the number of customers in each category
"""

# Create constants to store the rate of each category
GROCERY_RATE = 10
FOOD_RATE = 5
OTHER_RATE = 20

# Import Pandas to read the files
import pandas as pd
# Import NumPy to use the array
import numpy as np

# Define function to calculate the points
def calculate_points(category, value):
  # Multiply the value by the rate of the category
  if category == 'grocery':
    total = value / GROCERY_RATE
  elif category == 'food':
    total = value / FOOD_RATE
  elif category == 'other':
    total = value / OTHER_RATE
  return total
   

# read the csv file of the spending of each customer in each category in the state of Utah
dataUtah = pd.read_csv('customer_spending_UT.csv');

# read the csv file of the spending of each customer in each category in the state of Nevada
dataNevada = pd.read_csv('customer_spending_NV.csv');

# Create NumPy array containing the points of each customer in the state of Utah
utahArray = np.array([{'grocery': dataUtah['grocery'], 'food': dataUtah['food'], 'other': dataUtah['other']}])

# Create NumPy array containing the points of each customer in the state of Nevada
nevadaArray = np.array([{'grocery': dataNevada['grocery'], 'food': dataNevada['food'], 'other': dataNevada['other']}])

# Get the length of the NumPy array that represents the state of Utah
utahCustomersSpendingRecords = len(utahArray[0]['grocery'])

# Get the length of the NumPy array that represents the state of Nevada
nevadaCustomersSpendingRecords = len(nevadaArray[0]['grocery'])

# Sum the length of the NumPy array that represents the state of Utah and Nevada
totalSpendingRecords = utahCustomersSpendingRecords + nevadaCustomersSpendingRecords

# Print the total number of customers in the state of Utah and Nevada
print('There are ' + str(utahCustomersSpendingRecords) + ' spending records for Utah customers.')
print('There are ' + str(nevadaCustomersSpendingRecords) + ' spending records for Nevada customers. \n')

# Concatenate the NumPy array that represents all the grocery purchases of the state of Utah and Nevada
totalSpentOnGroceriesArray = np.concatenate([nevadaArray[0]['grocery'], utahArray[0]['grocery']])

# Concatenate the NumPy array that represents all the food purchases of the state of Utah and Nevada
totalSpentOnFoodArray = np.concatenate([nevadaArray[0]['food'], utahArray[0]['food']])

# Concatenate the NumPy array that represents all the other purchases of the state of Utah and Nevada
totalSpentOnOtherArray = np.concatenate([nevadaArray[0]['other'], utahArray[0]['other']])

# Create list to store the total points of customers in the state of Utah and Nevada by category
totalPointsPerCustomer = []

# Loop through all customers purchases
for i in range(totalSpendingRecords):
  # Calculate the points for each customer using the calculate_points function
  totalPointsPerCustomer.append(calculate_points('grocery', totalSpentOnGroceriesArray[i]) + calculate_points('food', totalSpentOnFoodArray[i]) + calculate_points('other', totalSpentOnOtherArray[i]))

# Create NumPy array to store the total points of customers in the state of Utah and Nevada
totalPointsPerCustomerArray = np.array(totalPointsPerCustomer)

# Calculate the mean of the points of all customers
meanOfPoints = round(totalPointsPerCustomerArray.mean(),2)

# Calculate the standard deviation of the points of all customers
stdOfPoints = round(totalPointsPerCustomerArray.std(),2)

# Calculate the median of the points of all customers
medianOfPoints =  round(np.median(totalPointsPerCustomerArray),2)

# Print the mean, standard deviation and median of the points of all customers
print('The mean of points earned is: '.ljust(55, ' ') + str(format(meanOfPoints, '.2f')))
print('The standard deviation of the of points earnded is: '.ljust(55, ' ') + str( format(stdOfPoints, '.2f')))
print('The median of points earnded is: '.ljust(55, ' ') + str( format(medianOfPoints, '.2f')) + '\n')

# Create mask to filter the customers that earned at least 700 points
planitumCustomers = (totalPointsPerCustomerArray >= 700)

# Create mask to filter the customers that earned 650 or more points and less than 700 points
goldCustomers = (totalPointsPerCustomerArray >= 650) & (totalPointsPerCustomerArray < 700)

# Create mask to filter the customers that earned 600 or more points and less than 650 points
siilverCustomers = (totalPointsPerCustomerArray >= 600) & (totalPointsPerCustomerArray < 650)

# Print the number of customers in the planitum category
print('Platinum customers: '.ljust(25, ' ') + str(planitumCustomers.sum()).rjust(5, ' '))

# Print the number of customers in the gold category
print('Gold customers: '.ljust(25, ' ') + str(goldCustomers.sum()).rjust(5, ' '))

# Print the number of customers in the silver category
print('Silver customers: '.ljust(25, ' ') + str(siilverCustomers.sum()).rjust(5, ' '))