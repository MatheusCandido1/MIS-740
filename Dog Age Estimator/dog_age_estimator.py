"""
# Dog Age Estimator
This application estimates the age of a dog in human years
Input: Dog's age in years
Output: Dog's age in humans years
Processing: 
1 - Get user input
2 - Validate user input
3 - Convert the dog's age in human years based on the table provided
4 - Show the dog's age in human years

* Author: Matheus Carvalho
* Date: 09-16-2022
"""

# Define function to get the Dog's age and convert to Human Years and return it
def getDogAgeEstimationInHumanYears(dogAge):
  if dogAge < 1:
    return '0 ~ 14'
  if dogAge < 2:
    return '15'
  if dogAge < 3:
    return '24'
  if dogAge < 4:
    return '28'
  if dogAge < 5:
    return '32'
  if dogAge == 5:
    return '37'
  return False

# Show name of application
print('Dog Age Estimator')

# Get the dog's age in years
dogAge = float(input('Please type the age of your dog: '))

# Validate if the input is valid 
if dogAge < 0:
  print('Invalid input, please try again')
  exit()

# Call the function to get the Human Years Estimate based on the input
humanYearsEstimate = getDogAgeEstimationInHumanYears(dogAge)

# Show the Dog's years in humas years
print('Your dog is approximately ' + humanYearsEstimate + ' years old in Human Years' if humanYearsEstimate else 'Human Year Unknown')
  