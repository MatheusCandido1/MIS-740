from controllers import candidate_controller, proposal_controller

def get_status(status):
    if status == 'PENDING':
        return '1'
    if status == 'ACCEPTED':
        return '2'
    if status == 'DECLINED':
        return '3'

def get_salary_suggestion():
  return ['1000', '2000']

def create_new_proposal():
  candidateId = input('Please enter the ID of the candidate: ')
  while candidateId == '':
    print('ID of the candidate cannot be empty.')
    candidateId = input('Please enter the ID of the candidate: ')

  candidate = candidate_controller.show(candidateId)
  if candidate == None:
    print('Candidate not found.')
    return
  
  
  print('\nSelected Candidate Information: ')
  print('Name: '.ljust(18), candidate[1])
  print('Address: '.ljust(18), candidate[2])
  print('Email: '.ljust(18), candidate[3])
  print('Phone: '.ljust(18), candidate[4])
  print('Experience Level: '.ljust(18), candidate[5])
  print('Remote Ratio:'.ljust(18), candidate[6])
  print('\nCreate New Proposal\n')

  proposal = {
    'candidate_id': candidateId,
    'job_title': '',
    'salary': '',
    'status': 'PENDING'
  }

  print('Please enter the job title:')
  proposal['job_title'] = input()

  if proposal['job_title'] == '':
    print('Job title cannot be empty.')
    proposal['job_title'] = input()

  print('For this candidate, we suggest the following salary range: U$' + str(get_salary_suggestion()[0]) + ' - U$' + str(get_salary_suggestion()[1]))

  print('Please enter the salary:')
  proposal['salary'] = input()
  if proposal['salary'] == '':
    print('Salary cannot be empty.')
    proposal['salary'] = input()

  proposal_controller.store(proposal)

def delete_proposal():
  print('Please enter the ID of the proposal you wish to delete.')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()

  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Proposal Date: '.ljust(18), currentProposal[2])
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])

    print('Are you sure you want to delete this proposal? (Y/N)')
    confirmation = input()
    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    if confirmation in ['Y', 'y']:
      proposal_controller.delete(proposalId)
  else:
    print('Proposal not found.')
  manage_proposals()

def view_proposal():
  print('Please enter the ID of the proposal you wish to view.')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()

  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Proposal Date: '.ljust(18), currentProposal[2])
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])
    print('Status: '.ljust(18), currentProposal[5])

    print('Would you like to visualize this proposal as a PDF? (Y/N)')
    confirmation = input()

    while confirmation not in ['Y', 'y', 'N', 'n']:
      print('Please enter a valid option: (Y/N)')
      confirmation = input()
    if confirmation in ['Y', 'y']:
      print('Generating PDF...')

  else:
    print('Proposal not found.')
  manage_proposals()

def update_existing_proposal():
  print('Please enter the ID of the proposal you wish to update.')
  proposalId = input()
  while proposalId == '':
    print('Proposal ID cannot be empty. Please enter again:')
    proposalId = input()

  currentProposal = proposal_controller.show(proposalId)
  if currentProposal:
    print('\nSelected Proposal Information: ')
    print('ID: '.ljust(18), currentProposal[1])
    print('Proposal Date: '.ljust(18), currentProposal[2])
    print('Job Title: '.ljust(18), currentProposal[3])
    print('Salary Offered: '.ljust(18), currentProposal[4])
    print('Status: '.ljust(18), currentProposal[5])

    updatedProposal = {
      'id': currentProposal[0],
      'candidate_id': currentProposal[1],
      'proposal_date': currentProposal[2],
      'job_title': currentProposal[3],
      'salary': currentProposal[4],
      'status': currentProposal[5]
    }

    updatedProposal['proposal_date'] = input("Proposal Date: (press enter if you don't want to update) ") or currentProposal[2]
    updatedProposal['job_title'] = input("Job Title: (press enter if you don't want to update) ") or currentProposal[3]
    updatedProposal['salary'] = input("Salary: (press enter if you don't want to update) ") or currentProposal[4]
    print("If updating proposals's status, please enter appropriate option:")
    print('1 - PENDING')
    print('2 - ACCEPTED')
    print('3 - DECLINED')
    statusOption = input("Status: (press enter if you don't want to update) ") or get_status(currentProposal[5])
    while statusOption not in ['1', '2', '3']:
      print ('Please enter a valid option:')
      statusOption = input()
    if statusOption == '1':
        updatedProposal['status'] = 'PENDING'
    elif statusOption == '2':
        updatedProposal['status'] = 'ACCEPTED'
    else:
        updatedProposal['status'] = 'DECLINED'
    proposal_controller.update(updatedProposal)

  else:
    print('Proposal not found.')

  manage_proposals()
  
def show_proposals_menu():
    print ('\nManage Proposals\n')
    print ('1 - Create New Proposal')
    print ('2 - View Proposal')
    print ('3 - Update Existing Proposal')
    print ('4 - Delete Existing Proposal')
    print ('5 - Go Back\n')

def manage_proposals():
  show_proposals_menu()

  print ('Please enter the option:')
  option = input()
      
  while option not in ['1', '2', '3', '4', '5']:
      print ('Please enter a valid option:')
      option = input()
  
  if option == '1':
    create_new_proposal()
  elif option == '2':
    view_proposal()
  elif option == '3':
    update_existing_proposal()
  elif option == '4':
    delete_proposal()