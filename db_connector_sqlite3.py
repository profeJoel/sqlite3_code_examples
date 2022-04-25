import sqlite3

con_db = sqlite3.connect('example.db')
cursor = con_db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tshirts
                        (sku text PRIMARY KEY, name text, size text, price real)''')

cursor.execute('''INSERT OR IGNORE INTO tshirts VALUES
                        ('SKU1234','Black Logo tshirt','Medium','24.99')''')

#cursor.execute('''INSERT INTO tshirts VALUES
#                        ('SKU1235','Black Logo tshirt','Large','24.99')''')

con_db.commit()

for row in cursor.execute('''SELECT * FROM tshirts'''):
    print(row)