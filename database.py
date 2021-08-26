import sqlite3
from words import nouns
import random

userId = [1,2,4,5,3]
priceList = [100, 150, 900, 879, 60, 3, 56, 7, 12, 33, 4, 509, 234, 325, 4, 5453, 45, 234, 2342, 64, 12, 724, 65]

def getRandomWord(li):
	return li[random.randint(0, len(li)-1)]

def randomGenerate(x):
	conn = sqlite3.connect('stockdb.db')
	id = 0

	ind = random.randint(0, len(priceList)-1)
	ind2 = random.randint(0, len(userId)-1)

	for i in range(x):
		conn.execute("INSERT INTO STOCKS (ID, NAME, CODE, PRICE, USERID) VALUES (?, ?, ?, ?, ?);", (id, getRandomWord(nouns), getRandomWord(nouns), getRandomWord(priceList), getRandomWord(userId)))
		id += 1

	conn.commit()
	conn.close()


conn = sqlite3.connect('stockdb.db')
print('Database Access Granted')

conn.execute(''' CREATE TABLE USERS
				(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                USERNAME TEXT NOT NULL,
				NAME TEXT NOT NULL,
				PASS TEXT NOT NULL);''')

conn.execute(''' CREATE TABLE STOCKS
				(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                USERID INTEGER NOT NULL,
				NAME TEXT NOT NULL,
				CODE TEXT NOT NULL,
				PRICE INT NOT NULL);''')


conn.execute("INSERT INTO USERS (ID, USERNAME, NAME, PASS) VALUES (1, 'Rahul0070', 'Rahul', '$5$rounds=535000$9wsJT07BXq4/Uz8z$QwklJGtU808BV/fekSDwFAu9NWx6Cei9It9KjyGZvLC');")

print('Table created.')
conn.commit()
conn.close()
randomGenerate(50)

print('Database populated.')