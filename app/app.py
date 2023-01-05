from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to my nameless gym app!'

if __name__ == "__main__":
    app.run(debug=True)