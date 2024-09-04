import sqlite3

# Establish a connection and a cursor with a database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on a condition
cursor.execute("SELECT * FROM events WHERE date ='2088.10.15' ")
row = cursor.fetchall()
print(row)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date ='2088.10.15' ")
row = cursor.fetchall()
print(row)

# Insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
           ('Hens', 'Hen City', '2088.10.17')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
row = cursor.fetchall()
print(row)
