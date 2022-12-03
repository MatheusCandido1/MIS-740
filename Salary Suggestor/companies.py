def show_companies_menu():
    print ('\nManage Company\n')
    print ('1 - Update Company Information')
    print ('2 - Go Back\n')

def manage_companies():
  show_companies_menu()

  print ('Please enter the option:')
  option = input()
      
  while option not in ['1', '2']:
      print ('Please enter a valid option:')
      option = input()