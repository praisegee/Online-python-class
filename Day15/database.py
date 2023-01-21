import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS password (id INTEGER, website VARCHAR(15), password VARCHAR(15))")

connection.commit()

connection.close()