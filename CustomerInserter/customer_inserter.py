"""
# Customer Inserter
This application connects to a database and inserts a new customer into the database if this customer is not already in the database.
Input: Customer number, name, address, city, state, and zip code
Output: Customer information or a message saying the customer was inserted
Processing:
1 - Connect to the database
2 - Select the CoffeeDB database
3 - Get user input for the customer number
4 - Validate user input for the customer number
5 - Check if the customer is already in the database
6 - If the customer is already in the database, show the customer information
7 - If the customer is not in the database, get user input for the customer name, address, city, state, and zip code
8 - Insert the customer into the database
9 - Commit the changes to the database
* Author: Matheus Carvalho
* Date: 11-30-2022
"""

# Import the mysql.connector module
import mysql.connector

# Create connection to the database
conn = mysql.connector.connect(
  host="localhost", # server
  user="root", # user name
  passwd="" #password
)
# Define cursor to execute queries
cursor = conn.cursor()

# Select the CoffeeDB database
cursor.execute('use CoffeeDB')

# Define function to insert a new customer into the database
def create_customer(customer):
  # Define query to insert a new customer into the database
  query = "INSERT INTO Customer (CustomerNumber, Name, Address, City, State, Zip) VALUES (%s, %s, %s, %s, %s, %s)"
  # Create a tuple with the customer information
  values = (customer['customerNumber'], customer['name'], customer['street'], customer['city'], customer['state'], customer['zipcode'])
  # Execute the query
  cursor.execute(query, values)
  # Commit the changes to the database
  conn.commit()
  # Print a message saying the customer was inserted
  print('row inserted.')

# Define function to check if the customer is already in the database
def customer_exists(customer_number):
  # Define query to check if the customer is already in the database
  cursor.execute("SELECT * FROM customer WHERE CustomerNumber = %s", (customer_number,))
  # Get the result of the query
  result = cursor.fetchone()
  # Check if the result is None
  if result == None:
    # If it is, return False
    return False
  else:
    # If not, return the customer information
    return result
# Get user input for the customer number
print('Please enter the customer number:')
customerNumber = input()

# Validate if the customer number is not blank
while customerNumber == '':
  print('The customer number cannot be empty, please enter again:')
  customerNumber = input()

# Call the function to check if the customer is already in the database and save the result in a variable 
customer = customer_exists(customerNumber)

# If the customer is not in the database, get user input for the customer name, address, city, state, and zip code
if not customer:
  print('Please enter the name: ')
  name = input()
  print('Please enter the street address: ')
  street = input()
  print('Please enter the city: ')
  city = input()
  print('Please enter the state: ')
  state = input()
  print('Please enter the zip: ')
  zipcode = input()
  # Overwirte customer variable with a dictionary with the customer information
  customer = {
    'customerNumber': customerNumber,
    'name': name,
    'street': street,
    'city': city,
    'state': state,
    'zipcode': zipcode
  }
  # Call the function to insert the customer into the database
  create_customer(customer)
  # If the customer is already in the database, show the customer information
else:
  print('The customer ' + customerNumber + ' exists already.')
  print('Name: ' + customer[1])
  print('Address: ' + customer[2] + ', ' + customer[3] + ', ' + customer[4] + ', ' + customer[5])