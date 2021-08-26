from flask import Flask, request, jsonify
from flask_cors import CORS
from transit import Transit

app = Flask(__name__)
CORS(app)
transit = Transit()

@app.route('/auth/', methods=['GET'])
def auth():
	
	username = request.args.get("username")
	password = request.args.get("pass")
	response = {}
	response["RESULT"] = transit.authenticate(username, password)
	return response



@app.route('/register', methods=['POST'])
def getInfo():
	data = request.get_json()
	print('here', data)
	name = data.get('name')
	username=data.get('username')
	
	password = data.get('password')
	

	res = transit.registerNewUser( username, name, password)
	if res == -1:
		return {'ERROR' : 'Data already exists.'}
	else:
		return {'RESULT' : 'Ok'}

@app.route('/getUser/', methods=['GET'])
def retrievContent():
	username = request.args.get("username")

	response = {}

	if username == None:
		response["ERROR"] = 'No username entered.'
	else:
		response = transit.getContent(username)

	return jsonify(response)

# @app.route('/getStockData/', methods=['GET'])
# def retrieveStock():
# 	userId = request.args.get("userId")

# 	response = {}
# 	if userId == None:
# 		response["ERROR"] = 'No user ID entered.'
# 	else:
# 		response = transit.getStockData(userId)

# 	return jsonify(response)

@app.route('/appendStock', methods=['POST'])
def addStock():
	
	data = request.get_json()
	
	userId = data.get('userId')
	name = data.get('name')
	code = data.get('code')
	price = data.get('price')
	

	res = transit.addStock(userId, name, code, price)
	if res == -1:
		return {'ERROR' : 'Data already exists.'}
	else:
		return {'MESSAGE' : 'Ok'}

@app.route('/getStocksPage/', methods=['GET'])
def getStocks():

	data = request.args
	sortBy = data.get("sortBy")
	quantity = data.get("quantity")
	offset = data.get("offset")
	userId = data.get("userId")

	response = {}
	response["RESULT"] = transit.getStocks(sortBy, quantity, offset, userId)
	response["SIZE"]= transit.getCount(userId)
	return response


@app.route('/getCount', methods=['GET'])
def getCount():
	response = {}
	userId = request.args.get("userId")
	response["RESULT"] = transit.getCount(userId)
	return response

@app.route('/getAll', methods=['GET'])
def getAll():
	return transit.getAll()

@app.route('/delStock', methods=['POST'])

def deleteStock():
	data =request.get_json()
	id = data.get('id')
	res = transit.deleteStock(id)
	if res == -1:
		return {'ERROR' : 'Data already exists.'}
	else:
		return {'MESSAGE' : 'Ok'}
	








if __name__ == '__main__':
	app.run(threaded=True, port=5000)