#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
import requests
from flask import Flask, Response, request
from flask_cors import CORS

application = Flask(__name__)
CORS(application, resources={r"/*": {"origins": "*"}})
@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)
@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)
@application.route('/calc/bit', methods=['GET'])
def post_currency_bit():
    return Response(json.dumps(get_bitcoin_index()), mimetype='application/json', status=200)
def get_bitcoin_index():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()['bpi']['USD']['rate']
    return response
# return generic data
@application.route('/get_generic', methods=['GET'])
def get_generic_data():
    return Response(json.dumps(generic_data), mimetype='application/json', status=200)
# mock data
currency_rate = {
    'usd' : 3.3,
    'pound' : 4.5,
    'euro' : 4.8
}
#generic data
generic_data = [
    {
    "id":1,
    "title": "wtf",
    "body": "good will"
    },
    {
    "id":2,
    "title": "wtf2",
    "body": "good will2"
    }
   ]
   
# get example for multiplication
# test get  
# curl -i http://"localhost:8000/v1/multiply?first_num=12.1&second_num=12"
@application.route('/v1/multiply', methods=['GET', 'POST'])
def get_mult_res():
    first_num = request.args.get('first_num')
    second_num = request.args.get('second_num')
    res = float(first_num) * float(second_num) 
    return Response(json.dumps({'multiplication result': res}), mimetype='application/json', status=200)
    
# get example for multiplication
# test get  
# curl -i http://"localhost:8000/v1/calcbit?first_num=5"
@application.route('/v1/calcbit', methods=['GET', 'POST'])
def get_mult_calc():
    first_num = request.args.get('first_num')
    second_num = get_bitcoin_index().replace(",", "")
    res = round(float(first_num) * float(second_num)) 
    return Response(json.dumps({'multiplication result': res}), mimetype='application/json', status=200)
    
if __name__ == '__main__':
    flaskrun(application)