from controllers import candidate_controller

def get_experience_level(experience_level):
    if experience_level == 'EN':
        return '1'
    if experience_level == 'MI':
        return '2'
    if experience_level == 'SE':
        return '3'
    if experience_level == 'EX':
        return '4'
    
def get_remote_ratio(remote_ratio):
    if remote_ratio == '0':
        return '1'
    if remote_ratio == '50':
        return '2'
    if remote_ratio == '100':
        return '3'
    
def show_candidates_menu():
    print ('\nManage Candidates\n')
    print ('1 - Create New Candidate')
    print ('2 - View Candidates')
    print ('3 - Update Existing Candidate')
    print ('4 - Delete Existing Candidate')
    print ('5 - Go Back\n')

def create_new_candidate():
    candidate = {
        'name': '',
        'address': '',
        'email': '',
        'phone': '',
        'experience_level': '',
        'remote_ratio': ''
    }
    
    print("Please enter candidate's name:")
    candidate['name'] = input()
    while candidate['name'] == '':
        print("Candidate's name cannot be empty.")
        print("Please enter candidate's name:")
        candidate['name'] = input()
        
    print("Please enter candidate's address:")
    candidate['address'] = input()
    while candidate['address'] == '':
        print("Candidate's address cannot be empty.")
        print("Please enter candidate's address:")
        candidate['address'] = input()
        
    print("Please enter candidate's email:")
    candidate['email'] = input()
    while candidate['email'] == '':
        print("Candidate's email cannot be empty.")
        print("Please enter candidate's email:")
        candidate['email'] = input()
        
    print("Please enter candidate's phone number:")
    candidate['phone'] = input()
    while candidate['phone'] == '':
        print("Candidate's phone number cannot be empty.")
        print("Please enter candidate's phone number:")
        candidate['phone'] = input()
        
    print("Please enter candidate's experience level:")
    print('1 - Entry Level')
    print('2 - Middle Level')
    print('3 - Senior Level')
    print('4 - Executive Level')
    experienceLevelOption = input()
    while experienceLevelOption not in ['1', '2', '3', '4']:
        print ('Please enter a valid option:')
        experienceLevelOption = input()
    if experienceLevelOption == '1':
        candidate['experience_level'] = 'EN'
    elif experienceLevelOption == '2':
        candidate['experience_level'] = 'MI'
    elif experienceLevelOption == '3':
        candidate['experience_level'] = 'SE'
    else:
        candidate['experience_level'] = 'EX'
        
    print("Is the candidate willing to work remotely?")
    print('1 - Not Open to Remote Work')
    print('2 - Open to Remote Work')
    print('3 - Only Open to Remote Work')
    remoteRatioOption = input()
    while remoteRatioOption not in ['1', '2', '3']:
        print ('Please enter a valid option:')
        remoteRatioOption = input()
    if remoteRatioOption == '1':
        candidate['remote_ratio'] = '0'
    elif remoteRatioOption == '2':
        candidate['remote_ratio'] = '50'
    else:
        candidate['remote_ratio'] = '100'
    candidate_controller.store(candidate)
    
def view_candidates():
    result = candidate_controller.index()
    if len(result) == 0:
        print('There are no candidates.')
    else:
        print("ID".ljust(3), "Name".ljust(20), "Address".ljust(20), "Email".ljust(20), "Phone".ljust(12), "Experience Level".ljust(2), "Remote Ratio".ljust(3))
        print('------------------------------------------------------------------------------------------------------------------------')
        for candidate in result:
            print(str(candidate[0]).ljust(3), str(candidate[1]).ljust(20), str(candidate[2]).ljust(20), str(candidate[3]).ljust(20), str(candidate[4]).ljust(12), str(candidate[5]).ljust(16), str(candidate[6]).ljust(3))
    
def update_existing_candidate(candidate):  
    updatedCandidate = {
        'id': candidate[0],
        'name': candidate[1],
        'address': candidate[2],
        'email': candidate[3],
        'phone': candidate[4],
        'experience_level': candidate[5],
        'remote_ratio': candidate[6]
    }
    print('Current Candidate Information: ')
    print('Name: '.ljust(18), candidate[1])
    print('Address: '.ljust(18), candidate[2])
    print('Email: '.ljust(18), candidate[3])
    print('Phone: '.ljust(18), candidate[4])
    print('Experience Level: '.ljust(18), candidate[5])
    print('Remote Ratio: '.ljust(18), candidate[6])
    updatedCandidate['name'] = input("Candidate Name: (press enter if you don't want to update) ") or candidate[1]
    updatedCandidate['address'] = input("Candidate Address: (press enter if you don't want to update) ") or candidate[2]
    updatedCandidate['email'] = input("Candidate Email: (press enter if you don't want to update) ") or candidate[3]
    updatedCandidate['phone'] = input("Candidate Phone: (press enter if you don't want to update) ") or candidate[4]
    print("If updating candidate's experience level, please enter appropriate option:")
    print('1 - Entry Level')
    print('2 - Middle Level')
    print('3 - Senior Level')
    print('4 - Executive Level')
    experienceLevelOption  = input("Candidate Experience Level: (press enter if you don't want to update) ") or get_experience_level(candidate[5])
    while experienceLevelOption not in ['1', '2', '3', '4']:
        print ('Please enter a valid option:')
        experienceLevelOption = input()
    if experienceLevelOption == '1':
        updatedCandidate['experience_level'] = 'EN'
    elif experienceLevelOption == '2':
        updatedCandidate['experience_level'] = 'MI'
    elif experienceLevelOption == '3':
        updatedCandidate['experience_level'] = 'SE'
    else:
        updatedCandidate['experience_level'] = 'EX'
    
    
    print("If updating the candidate's willingness to work remotely, please enter the appropriate option.")
    print('1 - Not Open to Remote Work')
    print('2 - Open to Remote Work')
    print('3 - Only Open to Remote Work')
    remoteRatioOption = input("Candidate Remote Ratio: (press enter if you don't want to update) ") or get_remote_ratio(candidate[6])
    while remoteRatioOption not in ['1', '2', '3']:
        print ('Please enter a valid option:')
        remoteRatioOption = input()
    if remoteRatioOption == '1':
        updatedCandidate['remote_ratio'] = '0'
    elif remoteRatioOption == '2':
        updatedCandidate['remote_ratio'] = '50'
    else:
        updatedCandidate['remote_ratio'] = '100'

    candidate_controller.update(updatedCandidate)
    
def go_back():
    print('Returning to main menu...')

def manage_candidates():
  show_candidates_menu()
  # beginning of main program
  # have user enter the corresponding number of the option they want to execute
  print ('Please enter the option:')
  option = input()
      
  # input validation: make sure user enters 
  while option not in ['1', '2', '3', '4', '5']:
      print ('Please enter a valid option:')
      option = input()

  if option == '1':
      create_new_candidate()

  elif option == '2':
      view_candidates()
      
  elif option == '3':
      print('Please enter the ID of the candidate you wish to update.')
      candidateId = input()
      while candidateId == '':
          print('Candidate ID cannot be empty. Please enter again:')
          candidateId = input()
      selectedCandidate = candidate_controller.show(candidateId)
      if selectedCandidate:
          update_existing_candidate(selectedCandidate)
      else:
          print('Candidate not found.')
          
  elif option == '4':
      print('Please enter the ID of the candidate you wish to delete.')
      candidateId = input()
      while candidateId == '':
          print('Candidate ID cannot be empty. Please enter again:')
          candidateId = input()
      if candidate_controller.show(candidateId):
          candidate_controller.delete(candidateId)
      else:
          print('Candidate not found.')
  else:
      go_back()