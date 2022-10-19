"""
# Height Converter
This application work as a simple height converter, converting centimeters to feet and inches.
Input: List of heights in centimeters
Output: List of heights in feet and inches
Processing:
1 - Locate the file with the list of heights in centimeters
2 - Open the file
3 - Read the file and store the values in a list
4 - Close the file
5 - Convert the list of heights in a NumPy array
6 - Create a new file to store the converted values
7 - Open the new file
8 - Convert the values from centimeters to feet and inches
9 - Write the converted values in the new file
10 - Close the new file
* Author: Matheus Carvalho
* Date: 10-19-2022
"""
# Import OS to use the path
import os

# Import NumPy to use the array
import numpy as np

# Create constants to facilitate further updates
CONVERT_RATE = 30.48

# Get the path of the file
path = os.path.join(os.path.dirname(__file__))

# Open the file in read mode using the path and filename 
file = open(path + '/heights_in_cm.txt', 'r')

# Read the file and store it in a list
heightsList = file.read().splitlines()

# Close the file
file.close()

# Convert the list to an NumPy array
heightsArray = np.array(heightsList, dtype='float32')

# Create a new file to store the converted values
newFile = open(path + '/heights_in_feet.txt', 'x')

# Loop through the heights array and convert the values
for height in heightsArray:
    # Get the feet value
    value = height / CONVERT_RATE
    # Get the inches value
    remainder = str(np.round(value - np.fix(value),1))[1:]

    # Write the converted value to the new file
    newFile.write(f'cm = {height} | ft = {int(value)}\'{remainder[1:3]}\"')

    # Add a new line to the file
    newFile.write(',\n')

# Close the new file
newFile.close()




