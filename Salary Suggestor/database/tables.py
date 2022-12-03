from connect import cursor

def create_tables():
  create_companies_table()
  create_candidates_table()
  create_proposals_table()

# Create table Companies
def create_companies_table():
  cursor.execute("CREATE TABLE IF NOT EXISTS companies (id int(11) primary key not null auto_increment, name VARCHAR(255), address VARCHAR(255), email VARCHAR(60), phone VARCHAR(20), color VARCHAR(7), description VARCHAR(255), benefits VARCHAR(255))")

# Create table Candidates
def create_candidates_table():
  cursor.execute("CREATE TABLE IF NOT EXISTS candidates (id int(11) primary key not null auto_increment, name VARCHAR(255), address VARCHAR(255), email VARCHAR(60), phone VARCHAR(20), experience_level VARCHAR(20), remote_ratio VARCHAR(20))")

# Create table Proposals
def create_proposals_table():
  cursor.execute("CREATE TABLE IF NOT EXISTS proposals (id int(11) primary key not null auto_increment, candidate_id int(11), proposal_date date default now(), job_title VARCHAR(100), salary float(10,2), status VARCHAR(20), foreign key (candidate_id) references candidates(id))")