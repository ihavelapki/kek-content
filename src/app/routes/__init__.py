import logging.config
from flask import request, Blueprint, jsonify
from ..lib import get_films


logger = logging.getLogger(__name__)
logger_line = '---|'

# create instance of Blueprint
logger.debug(f'{logger_line} before created blueprint')
films_bp = Blueprint('films', __name__)
logger.debug(f'{logger_line} after created blueprint')


@films_bp.route("/")
def hello():
    logger.debug(f'{logger_line} Hello run')
    n = 5
    film_list = get_films(n)
    # response = jsonify([{'id': 1, 'year': 2000, 'desc': 'Hello, I am from Russia', 'title': 'aaaa'}, {'id': 2, 'year': 2000, 'desc': 'balalana', 'title': 'aaaa'}])
    response = jsonify(film_list)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @films_bp.route('/films', methods=['GET', 'POST'])
# def get_films():
#
#     if request.method == 'GET':
#         password = request.args.get('pass').lower()
#     elif request.method == 'POST':
#         print('This is a POST')
#     else:
#         return {'err': 'err'}, 500
#
#     return {'First arg': 'value'}


@films_bp.route("/getpass")
def getpass():
    passwrd = request.args.get('pass').lower()
    response = jsonify({'your password is': f'{passwrd}'})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
