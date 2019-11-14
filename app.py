from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'home'


@app.route('/listen')
def listen():
    return 'music route'


@app.route('/update')
def update():
	return 'add some tunes'


