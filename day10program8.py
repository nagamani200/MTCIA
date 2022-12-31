import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE   Cars(
        Id INT,Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',32642)")
cur.execute("INSERT INTO Cars VALUES(2,'Skada',82642)")
cur.execute("INSERT INTO Cars VALUES(3,'Bentley',92646)")
cur.execute("INSERT INTO Cars VALUES(4,'Citrogen',42649)")
cur.execute("INSERT INTO Cars VALUES(5,'Hummer',57642)")
cur.execute("INSERT INTO Cars VALUES(6,'Volskwagan',62640)")
cur.execute("INSERT INTO Cars VALUES(7,'Mercedes',82642)")
con.commit()
print("values in table car inserted.")
