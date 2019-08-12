import sqlite3
import pandas as pd

# Bring data into a df
df = pd.read_csv('buddymove_holidayiq.csv')

# Check the data quality
print('DataFrame has:', df.shape[0], 'rows, and', df.shape[1], 'columns')
print('There are:', df.isna().sum().sum(), 'NaN values')

# Open a new connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# Send df to sqlite3 table
df.to_sql('buddymove_holidayiq', conn)

# Test connection
print('The head of the df should match the search query')

# print df
print(df.head())

# print table query results
curs = conn.cursor()
query = '''SELECT * FROM buddymove_holidayiq LIMIT 5'''
curs.execute(query)
print(curs.fetchall())