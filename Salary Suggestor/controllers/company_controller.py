from database import connect

def index():
  connect.cursor.execute("SELECT * FROM companies limit 1")
  result = connect.cursor.fetchall()
  return result

def update(company):
  sql = "UPDATE companies SET name = %s, address = %s WHERE id = %s"
  val = (company['name'], company['address'], company['id'])
  connect.cursor.execute(sql, val)
  connect.db.commit()
  print('Company information updated!')