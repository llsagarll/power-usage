'''Coded By SagaR'''
from flask import Flask
import flask
import json
from datetime import datetime
from flask_cors import CORS, cross_origin
import os



def power():
	
	x=os.popen("echo - | awk \"{printf  \
	$(( \
	$(cat /sys/class/power_supply/BAT1/current_now) * \
	$(cat /sys/class/power_supply/BAT1/voltage_now) \
	)) / 1000000000000 }\"").read()
	#print(x)
	x=str(x)
	now=datetime.now()
	time = now.strftime("%Y/%m/%d %H:%M:%S")
	d=[]
	d.insert(0,{"time":time})
	d.insert(1,{"power":str(x)}) 
	
	return d




from flask import Flask, send_file, make_response
app = Flask(__name__)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)
#api = Api(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response



@app.route('/', methods=['GET'])
def data_matrix():
  return flask.jsonify(power())


if __name__ == '__main__':
	app.run(host = '0.0.0.0',port=5000)

