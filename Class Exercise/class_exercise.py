# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:49:08 2022

@author: Matheus Carvalho
"""
def getBMILabel(bmi): 
  if bmi <= 18.5:
    return 'Under weight'
  if bmi <= 24.9:
    return 'Normal'
  if bmi <= 29.9:
    return 'Over Weight'
  if bmi <= 34.9:
    return 'Obesity (Class I)'
  if bmi <= 39.9:
    return 'Obesity (Class II)'
  if bmi > 40:
    return 'Extreme Obesity'

print('BMI Calculator')

height = float(input('Your Height (in inches): '))
weight = float(input('Your Weigth (in pounds): '))

if height <= 0 or weight <= 0:
  print('Invalid input, please try again!')
  exit()
  
heightConvertedToMeters = height / 39.37
weightConvertedToKilograms = weight / 2.205

bmi = weightConvertedToKilograms / pow(heightConvertedToMeters,2)

print('Your BMI is ' + str(round(bmi,1)) + ' and your classification is ' + getBMILabel(bmi))