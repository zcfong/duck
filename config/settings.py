from unipath import Path
from decouple import config


class Config:
    DEBUG = config('DEBUG', default=False, cast=bool)

    PROJECT_DIR: Path = Path(__file__).parent.parent
    READ_DATA_DIR: Path = PROJECT_DIR.child('data')
    READ_SCRIPT_DIR: Path = PROJECT_DIR.child('scripts')

    REDIS_URL = config('REDIS_URL')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

    @staticmethod
    def init_app(app):
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
