from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', title="Hello Flask", name=name)

@app.route('/hello_query_string')
def hello_query():
    name = request.args.get('name')
    return render_template('hello.html', title='Hello Query Flask', name=name)

@app.route('/hello_json')
def hello_json():
    return jsonify({'greeting': 'こんにちわ！'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)