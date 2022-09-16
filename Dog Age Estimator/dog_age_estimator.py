"""
# Dog Age Estimator
This application estimates the age of a dog in human years
Input: Dog's age in years
Output: Dog's age in humans years
Processing: 
1 - Get user input

* Author: Matheus Carvalho
* Date: 09-15-2022
"""

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
  if dogAge < 6:
    return '37'
  return False

dogAge = float(input('Please type the age of your dog (in years): '))

if dogAge < 0:
  print('Invalid input, please try again')
  exit()

humanYearsEstimate = getDogAgeEstimationInHumanYears(dogAge)

print('Your dog is approximately ' + humanYearsEstimate + ' years old in Human Years' if humanYearsEstimate else 'Human Year Unknown')
  