import connect

def companies_seeder():
  query = 'INSERT INTO companies (name, address, city, color, benefits, employees) VALUES (%s, %s, %s, %s, %s, %s)'
  values = (
    'UNLV', 
    '4505 S Maryland Pkwy', 
    'Las Vegas', 
    '#cf2030', 
    "Full family medical coverage will be provided through our company's employee benefit plan and will be effective on June 1. Dental and optical insurance are also available. The company offers a flexible paid time-off plan which includes vacation, personal and sick leave. Time off accrues at the rate of one day per month for your first year, then increased based on your tenure with the company. Eligibility for the company retirement plan begins 90 days after your start date",
    12000)
  connect.cursor.execute(query, values)
  connect.db.commit()
  print('DB Populated.')
