"""
# School Financial Data
This application provides a chart showing the Debt Ratio of 4 divisions of the United States.
Input: none
Output: Chart showing the Debt Ratio of 4 divisions of the United States.
1 - Open the file containig the population of each state per year.
2 - Set the index to the state abbreviation.
3 - Divide the2016  population of every state in by 1.000.000
4 - Open the file containig the information about the state such as Name, Abbreviation and Division
5 - Set the index to the state abbreviation.
6 - Open the file containig the Debt outstanding at end of fiscal year ($1,000) and Total revenue ($1,000)
7 - Fill the NaN values with 0
8 - Calculate the Debt Ratio by dividing the Debt outstanding at end of fiscal year by the Total revenue
9 - Get only the columns that contain the Debt Ratio and the year  from the Debt Ratio dataframe
10 - Create mask to get only the Debt Ratio of 2016
11 - Apply the mask to the Debt Ratio dataframe
12 - Merge the population data and the state data
13 - Merge the Debt Ratio data and the merged data from the previous step
14 - Format the Debt Ratio column to 2 decimal places
15 - Create a mask to get only the states that are in the Northeast, South, West and Midwest
16 - Plot scatter plot with the Debt Ratio and the population of the states in the Northeast, South, West and Midwest using the mask created in the previous step
17 - Set the title of the chart
18 - Set the x label of the chart
19 - Set the y label of the chart
20 - Display the legends
21 - Show the chart
* Author: Matheus Carvalho
* Date: 11-29-2022
"""
import pandas as pd
import matplotlib.pyplot as plt

populationData= pd.read_csv('nst-est2019-alldata.csv')
populationData = populationData.set_index('State/Region')

populationData = populationData[['Populatoin 2016']] / 1000000

stateDivision = pd.read_csv('state-division.csv')
stateDivision = stateDivision.set_index('abbreviation')

stateData = pd.read_csv('SSF_2014-2016_00A01_with_ann.csv')
stateData = stateData.set_index('Geographic area name')

cleanedStateData = stateData.fillna(0)
cleanedStateData['DebtRatio'] = cleanedStateData['Debt outstanding at end of fiscal year ($1,000)'].astype(int) / cleanedStateData['Total revenue ($1,000)'].astype(int)
cleanedStateData = cleanedStateData.fillna(0)
cleanedStateData = cleanedStateData[['Year','DebtRatio']]

yearMask = cleanedStateData['Year'] == 2016
cleanedStateData = cleanedStateData[yearMask]

mergedPopulationAndStateInformation = pd.merge(populationData, stateDivision, left_index=True, right_index=True)

mergedPopulationInformationAndDebtRatio = pd.merge(mergedPopulationAndStateInformation, cleanedStateData, how='inner', left_on='state', right_on='Geographic area name')
mergedPopulationInformationAndDebtRatio['DebtRatio'] = round(mergedPopulationInformationAndDebtRatio['DebtRatio'],2)

west = mergedPopulationInformationAndDebtRatio['Division'] == 'West'
northeast = mergedPopulationInformationAndDebtRatio['Division'] == 'Northeast'
south = mergedPopulationInformationAndDebtRatio['Division'] == 'South'
midwest = mergedPopulationInformationAndDebtRatio['Division'] == 'Midwest'


plt.scatter(mergedPopulationInformationAndDebtRatio['DebtRatio'][west], mergedPopulationInformationAndDebtRatio['Populatoin 2016'][west], label = 'West', alpha = 0.5)
plt.scatter(mergedPopulationInformationAndDebtRatio['DebtRatio'][northeast], mergedPopulationInformationAndDebtRatio['Populatoin 2016'][northeast], label = 'Northeast', alpha = 0.5)
plt.scatter(mergedPopulationInformationAndDebtRatio['DebtRatio'][south], mergedPopulationInformationAndDebtRatio['Populatoin 2016'][south], label = 'South', alpha = 0.5)
plt.scatter(mergedPopulationInformationAndDebtRatio['DebtRatio'][midwest], mergedPopulationInformationAndDebtRatio['Populatoin 2016'][midwest], label = 'Midwest', alpha = 0.5)

plt.title('School Finance and Population in 2016')
plt.xlabel('Debt Ratio (debt/revenue)')
plt.ylabel('Population (milion)')
plt.legend()