from config import FlaskConfig
from src.app import create_app
from flask import request

from flask import jsonify
from flask_cors import CORS
app = create_app(FlaskConfig)
CORS(app)


@app.route("/")
def hello():
    responce = jsonify([{'id': 1, 'year': 2000, 'desc': 'Hello, I am from Russia', 'title': 'aaaa'}, {'id': 2, 'year': 2000, 'desc': 'balalana', 'title': 'aaaa'}])
    responce.headers.add('Access-Control-Allow-Origin', '*')
    print(responce.headers)
    return responce


@app.route("/getpass")
def getpass():
    passwrd = request.args.get('pass').lower()
    print(passwrd)
    responce = jsonify({'your password is': f'{passwrd}'})
    responce.headers.add('Access-Control-Allow-Origin', '*')
    print(responce.headers)
    return responce


if __name__ == '__main__':
    # app.run(host='62.168.170.165')
    app.run(host='0.0.0.0')
