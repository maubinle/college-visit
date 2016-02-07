from flask import Flask
from flask import render_template
from flask import request
from flask import abort, redirect, url_for
import json
import urllib2



app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/test')
def get_json(): 
	response = urllib2.urlopen('http://nearbycolleges.info/api/autocomplete?q=university%20of%20i&limit=3')
	json_string = response.read()
	parsed_json = json.loads(json_string)
	print json_string


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test/')
def test_page():
	return "Page 2"





if __name__ == '__main__':
    app.run(debug=True)