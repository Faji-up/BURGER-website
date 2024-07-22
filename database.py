import sqlite3
import datetime

#con = sqlite3.connect("Users.db")
con = sqlite3.connect("Transactions.db")

c = con.cursor()
#exe = "CREATE TABLE transactions(id INTEGER PRIMARY KEY,prod text,payment INTEGER,date text,buyer_id INTEGER)"
#exe = "DROP TABLE transactions"
#c.execute(exe)
exe = "INSERT INTO transactions(prod, payment, date, buyer_id) VALUES (?, ?, ?, ?)"
c.execute(exe, ('CHEESY BACON BAGA', 91,str(datetime.date.today()) , 1))
con.commit()
con.close()