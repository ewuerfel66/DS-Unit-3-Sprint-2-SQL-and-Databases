import pandas as pd
import psycopg2


# Credentials
dbname = 'wifeyudd'
user = 'wifeyudd'
password = 'nSmG8Gl4wAtWglk2U2swUi_iMdOjzS30' # Don't commit this!
host = 'raja.db.elephantsql.com'


# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                       password=password, host=host)


# Instantiate cursor
pg_curs = pg_conn.cursor()


# How many survived?
query = """SELECT COUNT(id) FROM titanic
WHERE survived = 1;"""

# Execute
pg_curs.execute(query)

# Print answer
print('Survived:', pg_curs.fetchone()[0])


# How many didn't survived?
query = """SELECT COUNT(id) FROM titanic
WHERE survived = 0;"""

# Execute
pg_curs.execute(query)

# Print answer
print('Died:', pg_curs.fetchone()[0])


# Count for each class
query = """SELECT class, COUNT(*) FROM titanic
GROUP BY class
ORDER BY class;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Class, Count)')
print(pg_curs.fetchall())


# Ave age for survived?
query = """SELECT AVG(age) FROM titanic
WHERE survived =1;"""

# Execute
pg_curs.execute(query)

# Print answer
print('Average age of those who survived:')
print(pg_curs.fetchone()[0])


# Ave age for died?
query = """SELECT AVG(age) FROM titanic
WHERE survived =0;"""

# Execute
pg_curs.execute(query)

# Print answer
print('Average age of those who died:')
print(pg_curs.fetchone()[0])


# Ave age by class
query = """SELECT class, AVG(age) FROM titanic
GROUP BY class
ORDER BY class;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Class, Average Age)')
print(pg_curs.fetchall())


# Ave fare by class
query = """SELECT class, AVG(fare) FROM titanic
GROUP BY class
ORDER BY class;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Class, Average Fare)')
print(pg_curs.fetchall())


# Ave fare by survival status
query = """SELECT survived, AVG(fare) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Survival Status, Average Fare)')
print(pg_curs.fetchall())


# Ave siblings & spouses by class
query = """SELECT class, AVG(sibling_spouse) FROM titanic
GROUP BY class
ORDER BY class;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Class, Average Spouses & Siblings)')
print(pg_curs.fetchall())


# Ave siblings & spouses by survival status
query = """SELECT survived, AVG(sibling_spouse) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Survival Status, Average Spouses & Siblings)')
print(pg_curs.fetchall())


# Ave parents & children by class
query = """SELECT class, AVG(parent_children) FROM titanic
GROUP BY class
ORDER BY class;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Class, Average Parents & Children)')
print(pg_curs.fetchall())


# Ave parents & children by survival status
query = """SELECT survived, AVG(parent_children) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# Execute
pg_curs.execute(query)

# Print answer
print('(Survival Status, Average Parents & Children)')
print(pg_curs.fetchall())


# Same name?
query = """SELECT name FROM
(SELECT name, COUNT(name) FROM titanic
GROUP BY name) AS name_counts
WHERE count > 1;"""

# Execute
pg_curs.execute(query)

# Print answer
print('Anybody with the same name?')
if pg_curs.fetchall() == []:
    print('Nope')
else:
    print('Yep')