import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

%matplotlib inline

def format_currency(value):
    return '{:,.2f}'.format(value)
    
def get_application_type_label(applicationType):
    if applicationType == '1':
        return 'Residential'
    if applicationType == '2':
        return 'Non-Residential'
    if applicationType == '3':
        return None

def mask_data_by_application_data(applicationType):
    if get_application_type_label(applicationType) is not None:
        applicationTypeMask = fullData['Sector'] ==  get_application_type_label(applicationType)
        maskedData = fullData[applicationTypeMask]
        return maskedData
    else:
        return fullData

def show_statistics_options():
    print('1. Residential')
    print('2. Non-residential')
    print('3. Skip the statistics')

def show_chart_options():
    print('A. For non-residential applications, show the regression of the total project cost and incentive')
    print('B. For residential applications, show the distribution of total project cost by project statys and purchase type')
    print('C. For residential applications, show scatter plots of internter quantity and the expected KWH production, for high, medium and low density counties')
    print('D. Pair plots for total project cost, incentive amount, county area, and application month, with purchase type as the segretator')
    print('Z. End the program')

def show_regression():
    maskedData = mask_data_by_application_data('2')
    sns.jointplot("total cost", "$Incentive", data=maskedData, kind="reg")

def show_distribution():
    maskedData = mask_data_by_application_data('1')
    grid = sns.FacetGrid(maskedData, row="Project Status", col="Purchase Type", margin_titles=True)
    grid.map(plt.hist, "total cost", bins=np.linspace(0,100000,12))

def show_scatter_plots():
    maskedData = mask_data_by_application_data('1')
    inverterQuality = maskedData['Total Inverter Quantity']
    hightDensityCounties = maskedData['Expected kWh Annual Production'] >= 100
    mediumDensityCounties = maskedData['Expected kWh Annual Production'] < 100
    lowDensityCounties = maskedData['Expected kWh Annual Production'] < 10
    
    plt.scatter(inverterQuality, hightDensityCounties, label="High Density Counties", alpha=0.5)
    plt.scatter(inverterQuality, mediumDensityCounties, label="Medium Density Counties", alpha=0.5)
    plt.scatter(inverterQuality, lowDensityCounties, label="Low Density Counties", alpha=0.5)
    
    plt.title('Inverter Quantity and Expected KMh Production')
    plt.ylabel('Expected KMh Production')
    plt.xlabel('Inverter Quantity')
    plt.legend()

def show_pair_plots():
    fullData = mask_data_by_application_data('3')
    filteredData = fullData[['Purchase Type', 'total cost','$Incentive','Area (sq mi)','Application_Month']]
    sns.pairplot(filteredData, hue="Purchase Type", height=2.5)
    
    
NYCOUNTYFILE = 'NY County.csv'
ZIPCODENYFILE = 'zip_code_NY.csv'
NYSERDAFILE = 'Solar_Electric_NYSERDA.csv'

countyData = pd.read_csv(NYCOUNTYFILE)
zipcodeData = pd.read_csv(ZIPCODENYFILE)
serdaData = pd.read_csv(NYSERDAFILE)

countyData = countyData.fillna(0)
zipcodeData = zipcodeData.fillna(0)
serdaData = serdaData.fillna(0)

addressData = pd.merge(countyData, zipcodeData, how="inner", left_on="County", right_on="County")

fullData = pd.merge(addressData, serdaData, how="inner", left_on="Zip Code", right_on="Zip Code")
fullData['total cost'] = fullData['Hardware Cost'] +  fullData['Labor Cost'] +  fullData['misc cost']

print('This program shows the statistics and data distribution for applicationis of solar electric program.')
print('What type of application would you like to see?')
show_statistics_options()

typeOfApplication = input()
while typeOfApplication not in ['1','2','3']:
    print('Please select')
    show_statistics_options()
    typeOfApplication = input()
    
if typeOfApplication in ['1','2']:
    maskedData = mask_data_by_application_data(typeOfApplication)
    print('Average total cost per project: ', format_currency(maskedData['total cost'].mean()))
    print('Average incentive per project: ', format_currency(maskedData['$Incentive'].mean()))
    print('Average months to complete: ', format_currency(maskedData['Application_Month'].mean()))

print('Please select one of the options below to see the data distribution:')
show_chart_options()
option = input().upper()

while option not in ['A', 'B', 'C', 'D', 'Z']:
    print('Please select A, B, C, D or Z')
    option = input().upper()

if option == 'A':
    show_regression()
elif option == 'B':
    show_distribution()
elif option == 'C':
    show_scatter_plots()
elif option == 'D':
    show_pair_plots()
elif option == 'Z':
    print('Program ends.')
    