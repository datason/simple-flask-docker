from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(2**9)
    return '<h1> Hello! Igoryan!</h1>'