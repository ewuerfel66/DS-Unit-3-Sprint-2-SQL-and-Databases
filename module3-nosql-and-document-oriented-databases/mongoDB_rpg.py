import pymongo
import sqlite3


# Make a connection
conn = sqlite3.connect('rpg_db-Copy1.sqlite3')


# Create a cursor
char_curs = conn.cursor()


# Get the whole table
query = '''SELECT * FROM charactercreator_character'''
data = char_curs.execute(query).fetchall()


# Using 3.4 connection string
client = pymongo.MongoClient("mongodb://admin:eYvDbc1I3UZ3lwZd@cluster0-shard-00-00-utxvb.mongodb.net:27017,cluster0-shard-00-01-utxvb.mongodb.net:27017,cluster0-shard-00-02-utxvb.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


for row in data:
    # Create the character doc for each row
    char_doc = {
        'id':row[0],
        'name':row[1],
        'level':row[2],
        'exp':row[3],
        'hp':row[4],
        'strength':row[5],
        'intelligence':row[6],
        'dexterity':row[7],
        'wisdom':row[8]
    }
    db.test.insert_one(char_doc)