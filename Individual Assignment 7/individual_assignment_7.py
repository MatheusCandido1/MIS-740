"""
# State Tax Income Calculator
This application 
Input: The abbreviation of the state and the year.
Output: The state tax income for the year and for the state.:
1 - Open the file containig the description of the state tax income.
2 - Read one file to get the list of valid states and their abbreviations.
3 - Get the abbreviation of the state from the user.
4 - Validate the abbreviation of the state
5 - Get the year of the state tax income from the user.
6 - Validate the year of the state tax income.
7 - Read the file that contains the state tax income for the year
8 - Clean the data using pandas 
9 - Merge the data from the tax income file with the data the description of the state tax income
10 -Filter the merged data using the state abbreviation entered by the user
11 - Print the state tax income for the year and for the state.
"""

# Import Pandas to read the files
import pandas as pd

# Import NumPy to use the array
import numpy as np

# Create dictionary to facilitate the reading of the files and to validate the user input
yearCode = {
  2018: 0,
  2019: 1,
  2020: 2,
  2021: 3
}

# Create list with all the filenames
filesList = ['FY2018-STC-Detailed-Table','FY2019','FY2020','FY2021']
# Create string with the files extensions
extension = '.csv'

# Concatenate the list with the extension to create the list with the filenames
filesList = [i + extension for i in filesList]

# Open the file that contains the code and description of the tax categories and set the index to the code
taxItemDescriptionDataFrame = pd.read_csv('taxitemcodesanddescriptions.csv').set_index('Item Code')

# Open the first file in the files list
taxTable2018 = pd.read_csv(filesList[0])

# Get all the states from the headers of the first file
statesList = list(taxTable2018.columns)

# Create tuple with the states, excluding the first column (Item Code)
validStates = tuple(statesList[1:])

# Ask the user to input the state
print("Please enter the abbreviation of a state to see the tax information")
state = input().upper()

# If the state is not in the valid states, ask the user to input a valid state
while state not in validStates:
    print("The state abbreviation is not valid, please enter again:")
    state = input().upper()

# Ask the user to input the year
print("Please enter the year (2018, 2019, 2020 or 2021)")
year = int(input())

# If the year is not in the valid years, ask the user to input a valid year
while year not in yearCode.keys():
    print("Currently, only the data for 2018, 2019, 2020 and 2021 are available, please enter again:")
    year = int(input())

# Open the tax file using the year that the user input
taxTable = pd.read_csv(filesList[yearCode[year]])

# Remove all the invalid values from the tax file and set the index to the Item
cleanedTaxTable = taxTable.fillna(0).set_index('item')
# Merge the tax file with the description file using the index (Item Code)
mergedData = pd.merge(taxItemDescriptionDataFrame, cleanedTaxTable, left_index=True, right_index=True)

# Get the description and the value for the state entered by the user and remove the index of the data merged
dataPerState = mergedData[['Description', state]].reset_index(drop=True)
# Print the state and align it to the right
print(state.rjust(60))
# Print "Description"
print("Description")

# Convert the description to a numpy array
taxDescriptionArray = np.array(dataPerState['Description'])
# Convert the values to a numpy array
stateTaxesValueArray = np.array(dataPerState[state], dtype=np.float64)
# Loop through the description array
for i in range(len(taxDescriptionArray)):
    # Print the description and the value aligning the value to the right and the description to the left
    print(taxDescriptionArray[i].ljust(50) + '' + str(float("{:.1f}".format(stateTaxesValueArray[i]))).rjust(10))