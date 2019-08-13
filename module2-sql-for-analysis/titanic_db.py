import pandas as pd
import psycopg2

# Import titanic.csv into a DataFrame
df = pd.read_csv('https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/raw/master/module2-sql-for-analysis/titanic.csv')

# Change age to int
def to_int(entry):
    return int(entry)

df['Age'] = df['Age'].apply(to_int)

# Clean name
def clean(entry):
    return entry.replace("'", "")

df['Name'] = df['Name'].apply(clean)

# Save the rows as an array for easy syntax later
dirty_rows = df.values

# Clean up rows
rows = []

for row in dirty_rows:
    rows.append(tuple(row))

# Credentials
dbname = 'wifeyudd'
user = 'wifeyudd'
password = '9VZANv6zUnd0CQ0oKhyeMPiaT7LJaf2c' # Don't commit this!
host = 'raja.db.elephantsql.com'

# Establish connection
pg_conn = psycopg2.connect(dbname=dbname, user=user,
                       password=password, host=host)

# Instantiate cursor
pg_curs = pg_conn.cursor()

# Create table statement
create_titanic_table = """
CREATE TABLE titanic (
id SERIAL PRIMARY KEY,
survived INT,
class INT,
name VARCHAR(100),
sex VARCHAR(10),
age INT,
sibling_spouse INT,
parent_children INT,
fare FLOAT
);
"""

# Execute table creation
pg_curs.execute(create_titanic_table)

# Loop over the array to write rows in the DB
for row in rows:
    insert = """
    INSERT INTO titanic
    (survived, class, name, sex, age, sibling_spouse, parent_children, fare)
    VALUES 
    """ + str(row) + ';'
    
    pg_curs.execute(insert)

# Save and finish session
pg_curs.close()
pg_conn.commit()