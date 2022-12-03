from database import connect

def store(candidate):
  query = "INSERT INTO candidates (name, address, email, phone, experience_level, remote_ratio) VALUES (%s, %s, %s, %s, %s, %s)"
  values = tuple(candidate.values())
  connect.cursor.execute(query, values)
  connect.db.commit()
  print('1 row inserted.')

def index():
  connect.cursor.execute("SELECT * FROM candidates")
  result = connect.cursor.fetchall()
  return result

def show(candidateId):
  query = 'SELECT * FROM candidates WHERE id = %s'
  value = (candidateId,)
  connect.cursor.execute(query, value)
  result = connect.cursor.fetchone()
  if result == None:
    return False 
  else:
    return result

def update(candidate):
  query = 'UPDATE candidates SET name = %s, address = %s, email = %s, phone = %s, experience_level = %s, remote_ratio = %s WHERE id = %s'
  attrs = list(candidate.values())
  candidateId = attrs[0]
  attrs.pop(0)
  attrs.append(candidateId)
  values = tuple(attrs,)
  connect.cursor.execute(query, values)
  connect.db.commit()
  print('1 row updated.')

def delete(candidateId):
  query = 'DELETE FROM candidates WHERE id = %s'
  value = (candidateId,)
  connect.cursor.execute(query, value)
  connect.db.commit()
  print('Candidate has been deleted.')