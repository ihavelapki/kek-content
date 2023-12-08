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
    resp = {'hello': 'world'}
    response = jsonify(resp)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@films_bp.route('/films', methods=['GET'])
def fetch_films():
    logger.debug(f'{logger_line} fetch_films run')
    if request.method == 'GET':
        id = request.args.get('id')
        count = request.args.get('count')
    else:
        logger.error(f'{logger_line} It\'s not GET request')
        return {'err': 'err'}, 500

    if id:
        film = get_films(1)
        response = jsonify(film)
        response.headers.add('Access-Control-Allow-Origin', '*')
    elif count:
        films = get_films(count)
        response = jsonify(films)
        response.headers.add('Access-Control-Allow-Origin', '*')
    else:
        films = get_films(10)
        response = jsonify(films)
        response.headers.add('Access-Control-Allow-Origin', '*')

    logger.debug(f'{logger_line} fetch_films end')

    return response


@films_bp.route("/getpass")
def getpass():
    passwrd = request.args.get('pass').lower()
    response = jsonify({'your password is': f'{passwrd}'})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
