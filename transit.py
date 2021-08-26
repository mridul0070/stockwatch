
import sqlite3

from passlib.hash import sha256_crypt


class Transit:
	def __init__(self):
		self.dbName = 'stockdb.db'

	def getConnection(self):
		return sqlite3.connect('stockdb.db')

		 
	def authenticate(self, username, password):
		print(username, password)
		conn = sqlite3.connect(self.dbName)
		cursor = conn.execute('SELECT PASS FROM USERS WHERE USERNAME=?', (username,))
		row = cursor.fetchall()
		conn.close()
		if len(row) == 0:
			return 'No_User'
		print(password,row[0][0])
		if sha256_crypt.verify(password,row[0][0]): return 'Success'
		else: return 'Wrong password'
		
		


	def registerNewUser(self, username, name, password):
		conn = sqlite3.connect(self.dbName)
		cursor = conn.execute('SELECT ID FROM USERS WHERE USERNAME = ?', (username,))
		data = cursor.fetchall()

		if len(data) == 0:
			conn.execute("INSERT INTO USERS ( USERNAME, NAME, PASS) VALUES ( ?, ?, ?);", ( username, name, sha256_crypt.encrypt(password)))
			conn.commit()
			conn.close()
			return 1

		else:
			print('Data already exists')
			conn.close()
			return -1

	def getContent(self, username):
		conn = sqlite3.connect(self.dbName)
		
		response = {}
		cursor = conn.execute("SELECT ID,USERNAME,NAME FROM USERS WHERE USERNAME=?", (username,))

		row = cursor.fetchall()
		conn.close()

		try:
			response["ID"] = row[0][0]
			response["USERNAME"] = row[0][1]
			response["NAME"] = row[0][2]
		except:
			response["ERROR"] = 'User not found'

		return response
		

	# def getStockData(self, userId):
	# 	conn = sqlite3.connect(self.dbName)
	# 	response = {}
	# 	cursor = conn.execute("SELECT ID, NAME, CODE, PRICE FROM STOCKS WHERE USERID=?", (userId,))
	# 	row = cursor.fetchall()
		
	# 	response["STOCKDATA"]= row
	# 	conn.close()
	# 	return response
	def getCount(self, userId):
		conn = self.getConnection()
		cursor = conn.execute('SELECT ID FROM STOCKS WHERE USERID=?', (userId,))
		row = cursor.fetchall()
		return len(row)

	def getAll(self):
		conn = self.getConnection()
		cursor = conn.execute('SELECT * FROM STOCKS')
		row = cursor.fetchall()
		response = {}
		response['RESULT'] = row
		return response 

	# def getStocks(self, sortBy, quantity, offset, userId):
	# 	conn = self.getConnection()
	# 	cursor = conn.execute(''' SELECT ID, NAME, CODE, PRICE 
	# 							FROM STOCKS
	# 							WHERE USERID=?
	# 							ORDER BY ?
	# 							LIMIT ?, ?''', (userId, sortBy, offset, quantity));

	# 	row = cursor.fetchall()

	# 	result = []
	# 	for i in row:
	# 		item = {
	# 		'id': i[0],
	# 		'name': i[1],
	# 		'code': i[2],
	# 		'price': i[3]
	# 		}
	# 		print(item)
	# 		result.append(item)

	# 	return result


	def getStocks(self, sortBy, quantity, offset, userId):
		conn = self.getConnection()
		statement = 'SELECT ID, NAME, CODE, PRICE FROM STOCKS WHERE USERID=? ORDER BY ' + sortBy + ' LIMIT ?, ?'

		cursor = conn.execute(statement, (userId, offset, quantity))

		row = cursor.fetchall()

		result = []
		for i in row:
			item = {
			'id': i[0],
			'name': i[1],
			'code': i[2],
			'price': i[3]
			}
			print(item)
			result.append(item)

		return result

	

	def addStock(self, userId, name, code, price):
		conn = sqlite3.connect(self.dbName)
		cursor = conn.execute("INSERT INTO STOCKS ( USERID, NAME, CODE, PRICE) VALUES (?, ?, ?, ?);", (userId, name, code, price))
		conn.commit()
		conn.close()
		return 1


	def deleteStock(self,id):
		conn = sqlite3.connect(self.dbName) 
		cursor = conn.execute('DELETE FROM STOCKS WHERE ID=?', (id,))
		conn.commit()
		conn.close()
		return 1






