from database import connect

def show(companyId):
  query = "SELECT * FROM companies WHERE id = %s"
  values = (companyId,)
  connect.cursor.execute(query, values)
  result = connect.cursor.fetchone()
  return result

def update(company):
  sql = "UPDATE companies SET name = %s, address = %s WHERE id = %s"
  val = (company['name'], company['address'], company['id'])
  connect.cursor.execute(sql, val)
  connect.db.commit()
  print('Company information updated!')