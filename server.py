from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test/')
def test_page():
	return "Page 2"

@app.route('/hello/')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)