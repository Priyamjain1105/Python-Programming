import sqlite3
conn = sqlite3.connect('database.db')
print( "Opened database successfully")
conn.execute('Create Table students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created Successfully");

