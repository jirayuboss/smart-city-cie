import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

import requests
import time

def check_fullbin(x):
	if x < 5:
		return 'Full'
	else:
		return 'Empty'

def bin_percentage(x):
	if x >= 43:
		return '100'
	else:
		percentage = (x/43)*100
		return str(percentage)
bin_color = ['Blue bin','Yellow bin','Red bin','Black bin']

@app.route('/smartbin/<location>')
def get_binstatus(location=None):
	url = "http://35.208.101.91:8080/sensors/project_id/smartbin/" + location
	response = requests.get(str(url))
        bin_status = response.json()
	data = []
	for i in range(len(bin_status)):
		new_data = {'name': bin_color[i], 'sensor_id':bin_status[i]["sensor_id"], 'status':check_fullbin(int(bin_status[i]["sensor_data"])), 'percentage': bin_percentage(int(bin_status[i]["sensor_data"])), 'location':bin_status[i]["location"]}
		data.append(new_data)
	return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
