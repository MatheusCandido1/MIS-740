print('First year salary: ')
salary = input()

print('Enter the the time you have taught (in Years): ')
years = input()

year = 1
lastYearSalary = 0;

while year <= int(years):
  if(year == 1):
   lastYearSalary = float(salary)
  elif(year >= 2 and year < 14):
    lastYearSalary = round(float(lastYearSalary) * 1.032,2)

  print('Year: ', year)
  print('Salary: ', lastYearSalary)
  year = year + 1
