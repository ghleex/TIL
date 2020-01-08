from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'what the heck'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'