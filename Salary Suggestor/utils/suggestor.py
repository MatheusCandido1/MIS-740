INITIAL_VALUE = 68238.97
LARGE_COMPANY = 26558.22
SMALL_COMPANY = 10393.38
CONTRACT = 29201.57
MID_LEVEL = 46865.08
SENIOR_LEVEL = 82697
EXECUTIVE_LEVEL = 135930.3

RANGE = 5000

def get_company_size(employees):
  if employees <= 49:
    return 'S'
  if employees >= 50 and employees <= 249:
    return 'M'
  if employees >= 250:
    return 'L'

def get_salary_suggestion(candidate, company):
  salary = INITIAL_VALUE
  companySize = get_company_size(int(company['employees']))

  if companySize == 'L':
    salary += LARGE_COMPANY
  elif companySize == 'S':
    salary += SMALL_COMPANY

  if candidate['experience_level'] == 'MI':
    salary += MID_LEVEL
  elif candidate['experience_level'] == 'SE':
    salary += SENIOR_LEVEL
  elif candidate['experience_level'] == 'EX':
    salary += EXECUTIVE_LEVEL

  if candidate['employment_type'] == 'CT':
    salary += CONTRACT

  return {
    'min': salary - RANGE,
    'max': salary + RANGE
  }
