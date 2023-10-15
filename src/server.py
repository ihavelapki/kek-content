import os
import yaml
import logging.config
# from dotenv import load_dotenv
from config import FlaskConfig
from src.app import create_app
from flask_cors import CORS


with open('config/logconfig.yml', 'r', encoding="utf-8") as f:
    log_config = yaml.load(f.read(), Loader=yaml.loader.SafeLoader)

logging.config.dictConfig(log_config)
logger = logging.getLogger('server')
logger_line = '-----------|'

logger.debug(f'{logger_line} Before created')
app = create_app(FlaskConfig)
CORS(app)

logger.debug(f'{logger_line} Created')


if __name__ == '__main__':
    # app.run(host='62.168.170.165')
    logger.debug('Poehali')
    app.run(host='0.0.0.0')

