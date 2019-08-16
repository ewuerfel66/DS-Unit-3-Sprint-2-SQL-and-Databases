import sqlite3


# Open connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


def query(string):
    curs.execute(string)

def save():
    curs.close()
    conn.commit()


# Create a table
query('''CREATE TABLE demo (s TEXT,
                              x NUMERIC,
                              Y numeric);''')



# Insert Rows
query('''INSERT INTO demo VALUES ('g', 3, 9);''')


query('''INSERT INTO demo VALUES ('v', 5, 7);''')

query('''INSERT INTO demo VALUES ('f', 8, 7);''')


# Check
query('''SELECT * FROM demo;''')
print('Data check:', curs.fetchall())


# Close connection
save()

####################################################

# Reopen connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


# How many rows?
query('''SELECT COUNT(*) FROM demo;''')

# Print answer
print('There are', curs.fetchone()[0], 'rows.')


# How many rows where x & y are at least 5?
query('''SELECT COUNT(*) FROM demo
WHERE x >= 5
AND y >= 5;''')

# Print answer
print('There are', curs.fetchone()[0], 'rows where x and y are at least 5.')


# How many unique values of y are there
query('''SELECT COUNT(DISTINCT y) FROM demo;''')

# Print answer
print('There are', curs.fetchone()[0], 'unique values of y.')