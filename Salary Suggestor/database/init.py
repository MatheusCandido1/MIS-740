from connect import cursor

def create_database():
  cursor.execute('CREATE DATABASE IF NOT EXISTS db_salarysuggestor')
  cursor.execute('USE db_salarysuggestor')