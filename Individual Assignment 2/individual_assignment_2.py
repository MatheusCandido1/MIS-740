# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:52:43 2022

@author: Matheus Carvalho
"""
# Define constants to facilitate further updates
UNLIMITED_CALLS_AND_TEXTS = 9.99
OLD_CUSTOMER_RATE = 9.50
NEW_CUSTOMER_RATE = 11.30

# Set function to format floats and integers to Currency Format
def formatCurrency(value):
  return '$' + str(format(value,'.2f'))

# Print initial message
print('The purpose of the program is to calculate the cell phone bill for customers of a cell phone company')

# Get data usage from user
print('Please enter the data usage last month in GB:')
dataUsage = float(input())

# Get account year from user
print('Please enter the year the account is opend:')
accountYear = float(input())

# Validate if the inputs are valid 
if dataUsage <= 0 or accountYear <= 0:
  print('Invalid input, please try again!')
  exit()

# Check if the user is an old or a new customer and apply the correct rate
if accountYear >= 2020:
  dataUsageSubtotal = dataUsage * NEW_CUSTOMER_RATE
else:
  dataUsageSubtotal = dataUsage * OLD_CUSTOMER_RATE

# Check if the data usage is above the limit to correct the charge
if dataUsageSubtotal > 30:
  dataUsageSubtotal = 30.00

# Sum the data usage with the default value for calls and texts
total = dataUsageSubtotal + UNLIMITED_CALLS_AND_TEXTS;

# Print all results
print('Calls and Texts: ' + formatCurrency(UNLIMITED_CALLS_AND_TEXTS))
print('Data: ' + formatCurrency(dataUsageSubtotal))
print('Total: ' + formatCurrency(total))