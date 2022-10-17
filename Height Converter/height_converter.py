"""
# Height Converter
Processing:
1 - Get user input
* Author: Matheus Carvalho
* Date: 10-17-2022
"""
import os
import numpy as np

CONVERT_RATE = 30.48

path = os.path.join(os.path.dirname(__file__))

file = open(path + '/heights_in_cm.txt', 'r')

heightsList = file.read().splitlines()

file.close()

heightsArray = np.array(heightsList, dtype='float32')


newFile = open(path + '/heights_in_feet.txt', 'x')

for height in heightsArray:
    value = height / CONVERT_RATE
    rest = str(np.round(value - np.fix(value),1)) [1:]
    newFile.write(f'cm = {height} | ft = {int(value)}\'{rest[1:3]}\"')
    newFile.write(',\n')

newFile.close()




