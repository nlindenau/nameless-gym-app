from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to my nameless gym app!'