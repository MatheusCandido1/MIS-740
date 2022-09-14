"""
# BMI Calculator Application
This application calculates the BMI of a human being
Input: Weight (in pounds) and Height (in inches) of the user
Output: BMI rate and classification
Processing: 
1 - Get user input
2 - Validate user input
3 - Convert the weight to kilograms and the height to meters
4 - Calculate the BMI using the following formula (weight/(height^2))
5 - Get the classification based on the BMI
6 - Show the BMI and the Classification to the user

* Author: Matheus Carvalho
* Date: 09-14-2022
"""
# Define constants to facilitate further updates
HEIGHT_CONVERT_RATE = 39.37
WEIGHT_CONVERT_RATE = 2.205

# Define function to get the Body Mass Index and return the classification
def getBodyMassIndexClassification(bodyMassIndex): 
  if bodyMassIndex <= 18.5:
    return 'Under weight'
  if bodyMassIndex <= 24.9:
    return 'Normal'
  if bodyMassIndex <= 29.9:
    return 'Over Weight'
  if bodyMassIndex <= 34.9:
    return 'Obesity (Class I)'
  if bodyMassIndex <= 39.9:
    return 'Obesity (Class II)'
  if bodyMassIndex > 40:
    return 'Extreme Obesity'

# Show name of application
print('BMI Calculator')

# Get the user's height
height = float(input('Please enter your height (in inches): '))

# Get the user's weight
weight = float(input('Please enter your height (in pounds): '))

# Validate if the inputs are valid 
if height <= 0 or weight <= 0:
  print('Invalid input, please try again!')
  exit()
  
# Convert height from inches to meters
heightConvertedToMeters = height / HEIGHT_CONVERT_RATE

# Convert weight from pounds to kilograms
weightConvertedToKilograms = weight / WEIGHT_CONVERT_RATE

# Calculate the Body Mass Index using the formula
bodyMassIndex = weightConvertedToKilograms / pow(heightConvertedToMeters,2)

# Show the Body Mass Index and its classification
print('Your BMI is ' + str(round(bodyMassIndex,1)) + ' and your classification is ' + getBodyMassIndexClassification(bodyMassIndex))