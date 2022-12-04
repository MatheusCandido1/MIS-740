import tables, init, seeds

init.create_database()

tables.create_tables()

seeds.companies_seeder()

