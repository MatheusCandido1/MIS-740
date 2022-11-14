"""
# Tax Caculator
This application 
Input: Files that contains the spending of each customer in each category in the state of Nevada and Utah.
Output: Mean, standard deviation and median of the points and how many customers in each category.
Processing:
1 - Read the files that contains the spending of each customer in each category in the state of Nevada and Utah from the user.
"""


# Import Pandas to read the files
# Import NumPy to use the array

import pandas as pd
import numpy as np

yearCode = {
  2018: 0,
  2019: 1,
  2020: 2,
  2021: 3
}

descriptionFile = 'taxitemcodesanddescriptions.csv'

filesList = ['FY2018-STC-Detailed-Table','FY2019','FY2020','FY2022']
extension = '.csv'

filesList = [i + extension for i in filesList]

taxItemDescriptionDataFrame = pd.read_csv(descriptionFile).set_index('Item Code')

taxTable2018 = pd.read_csv(filesList[0])

statesList = list(taxTable2018.columns)

validStates = tuple(statesList[1:])
validYears = (2018, 2019, 2020, 2021)

print("Please enter the abbreviation of a state to see the tax information")
state = input().upper()

while state not in validStates:
    print("The state abbreviation is not valid, please enter again:")
    state = input().upper()

print("Please enter the year (2018, 2019, 2020 or 2021)")
year = int(input())

while year not in validYears:
    print("Currently, only the data for 2018, 2019, 2020 and 2021 are available, please enter again:")
    year = int(input())

taxTable = pd.read_csv(filesList[yearCode[year]])
cleanedTaxTable = taxTable.fillna(0).set_index('item')
mergedData = pd.merge(taxItemDescriptionDataFrame, cleanedTaxTable, left_index=True, right_index=True)
dataPerState = mergedData[['Description', state]].reset_index(drop=True)
print(state.rjust(60))
print("Description")
taxDescriptionArray = np.array(dataPerState['Description'])
stateTaxesValueArray = np.array(dataPerState[state], dtype=np.float64)
for i in range(len(taxDescriptionArray)):
    print(taxDescriptionArray[i].ljust(50) + '' + str(float("{:.1f}".format(stateTaxesValueArray[i]))).rjust(10))