from database import connect

def store(proposal):
  sql = "INSERT INTO proposals (candidate_id, job_title, salary, status) VALUES (%s, %s, %s, %s)"
  values = tuple(proposal.values())
  connect.cursor.execute(sql, values)
  connect.db.commit()
  
  print("1 row inserted.")

def index():
  connect.cursor.execute("SELECT * FROM proposals")
  result = connect.cursor.fetchall()
  return result

def show(id):
  sql = "SELECT proposals.id as proposal_id, candidate_id, proposal_date, job_title, salary, status, name, address, experience_level, employment_type FROM proposals INNER JOIN candidates ON proposals.candidate_id = candidates.id WHERE proposals.id = %s"
  val = (id,)
  connect.cursor.execute(sql, val)
  result = connect.cursor.fetchone()
  return result

def update(proposal):
  query = "UPDATE proposals SET candidate_id = %s, proposal_date = %s, job_title = %s, salary = %s, status = %s WHERE id = %s"
  attrs = list(proposal.values())
  proposalId = attrs[0]
  attrs.pop(0)
  attrs.append(proposalId)
  values = tuple(attrs,)
  connect.cursor.execute(query, values)
  connect.db.commit()
  print('1 row updated.')

def delete(proposalId):
  query = 'DELETE FROM proposals WHERE id = %s'
  value = (proposalId,)
  connect.cursor.execute(query, value)
  connect.db.commit()
  print('Proposal has been deleted.')