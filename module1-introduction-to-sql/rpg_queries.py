import sqlite3

# Make a connection
conn = sqlite3.connect('rpg_db.sqlite3')

# Create a cursor for Character Questions
char_curs = conn.cursor()

# How many characters?
query = '''SELECT COUNT(character_id) FROM charactercreator_character'''
char_curs.execute(query)

# Print answer
print('There are', char_curs.fetchone()[0], 'characters')

# How many mages?
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_mage'''
char_curs.execute(query)

# Print answer
print('There are', char_curs.fetchone()[0], 'mages')

# How many thiefs?
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_thief'''
char_curs.execute(query)

# Print answer
print('There are', char_curs.fetchone()[0], 'thieves')

# How many clerics?
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_cleric'''
char_curs.execute(query)

# Print answer
print('There are', char_curs.fetchone()[0], 'clerics')

# How many fighters?
query = '''SELECT COUNT(character_ptr_id) FROM charactercreator_fighter'''
char_curs.execute(query)

# Print answer
print('There are', char_curs.fetchone()[0], 'fighters')

# Create a cursor for Character Questions
item_curs = conn.cursor()

# How many items?
query = '''SELECT COUNT(item_id) FROM armory_item'''
item_curs.execute(query)

# Print answer
print('There are', item_curs.fetchone()[0], 'items')

# How many weapons?
query = '''SELECT COUNT(item_ptr_id) FROM armory_weapon'''
item_curs.execute(query)

# Print answer
print('There are', item_curs.fetchone()[0], 'weapons')

# How many non-weapons
print(174 - 37, 'are NOT weapons')

# How many items does each character have?
query = '''SELECT cc.name, COUNT(ci.item_id) FROM charactercreator_character_inventory as ci 
JOIN charactercreator_character as cc ON cc.character_id = ci.character_id 
GROUP BY ci.character_id LIMIT 20'''
item_curs.execute(query)

# Print answer
print('(Character, Amount of Items)')
print(item_curs.fetchall())