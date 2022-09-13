# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:49:08 2022

@author: Matheus Carvalho
"""
def getBMILabel(BMI): 
  if BMI <= 18.5:
    return 'Under weight'
  if BMI <= 24.9:
    return 'Normal'
  if BMI <= 29.9:
    return 'Over Weight'
  if BMI <= 34.9:
    return 'Obesity (Class I)'
  if BMI <= 39.9:
    return 'Obesity (Class II)'
  if BMI > 40:
    return 'Extreme Obesity'

print('BMI Calculator')

print('Your Height (in inches): ')
height = input()

print('Your Weigth (in pounds): ')
weight = input()

heightConvertedToMeters = float(height) / 39.37
weightConvertedToKilograms = float(weight) / 2.205

BMI = weightConvertedToKilograms / pow(heightConvertedToMeters,2)

print('Your IBM is ' + str(round(BMI,1)) + ' and your classification is ' + getBMILabel(BMI))