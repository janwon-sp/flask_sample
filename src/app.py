from flask import Flask
from flask import render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)