from flask import Flask

app = Flask(__name__)

def hello():
    return 'Hello from the other side of docker!'

app.add_url_rule('/', '/', hello)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
