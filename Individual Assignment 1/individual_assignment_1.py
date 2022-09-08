print('First year salary: ')
salary = input()

print('Enter the the time you have taught (in Years): ')
years = input()
salariesByYear= [];

salariesByYear.append(
  {
    'year': 1,
    'salary': round(int(salary),2)
  }
);

for year in range(0, int(years)-1):
  data = {
    'year': salariesByYear[year]['year'] + 1,
    'salary': round((salariesByYear[year]['salary'] * 1.032),2) if year < 13 else round((salariesByYear[12]['salary'] * 1.032),2)
  }
  salariesByYear.append(data)
