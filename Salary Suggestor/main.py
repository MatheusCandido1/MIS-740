"""
* Author: Matheus Carvalho
* Date: 09-28-2022
"""

from controllers import company_controller
import candidates, proposals, companies

def welcome(company):
  print('\nCompany Information:')
  print('Name:'.ljust(8) , company[1])
  print('Address:'.ljust(8), company[2])

def show_main_menu():
  print('\nMenu:')
  print('1 - Manage Company')
  print('2 - Manage Candidates')
  print('3 - Manage Proposals')
  print('4 - Exit \n')



def bootstrap():
  companyId = 1
  company = company_controller.show(companyId)
  welcome(company)

  show_main_menu()
  option = input()

  while option != '4':
    if option == '1':
      companies.manage_companies()
    if option == '2':
      candidates.manage_candidates()
    if option == '3':
      proposals.manage_proposals(company)

  if option == '4':
    print('Thank you for using our software!')
    exit()

bootstrap()
