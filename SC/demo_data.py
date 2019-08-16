import sqlite3


# Open connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# Create a table
query = '''CREATE TABLE demo (s TEXT,
                              x NUMERIC,
                              Y numeric);'''
curs.execute(query)


# Insert Rows
query = '''INSERT INTO demo VALUES ('g', 3, 9);'''
curs.execute(query)

query = '''INSERT INTO demo VALUES ('v', 5, 7);'''
curs.execute(query)

query = '''INSERT INTO demo VALUES ('f', 8, 7);'''
curs.execute(query)


# Check
query = '''SELECT * FROM demo;'''
curs.execute(query)
print('Data check:', curs.fetchall())


# Close connection
curs.close()
conn.commit()

####################################################

# Reopen connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# How many rows?
query = '''SELECT COUNT(*) FROM demo;'''
curs.execute(query)

# Print answer
print('There are', curs.fetchone()[0], 'rows.')


# How many rows where x & y are at least 5?
query = '''SELECT COUNT(*) FROM demo
WHERE x >= 5
AND y >= 5;'''
curs.execute(query)

# Print answer
print('There are', curs.fetchone()[0], 'rows where x and y are at least 5.')


# How many unique values of y are there
query = '''SELECT COUNT(DISTINCT y) FROM demo;'''
curs.execute(query)

# Print answer
print('There are', curs.fetchone()[0], 'unique values of y.')