import sqlite3
conn=sqlite3.connect('scores.db')
print("Opened database successfully")
conn.execute('CREATE TABLE scores (name TEXT, score TEXT)')
print("Table created successfully")
conn.close()
