import logging.config
from flask import Flask

logger = logging.getLogger(__name__)
logger_line = '----------|'


def create_app(config):
    logger.debug(f'{logger_line} this is a {__name__}')
    app = Flask(__name__)
    app.config.from_object(config)

    from .routes import films_bp
    app.register_blueprint(films_bp)

    return app
