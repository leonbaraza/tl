import secrets


class Config():
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Leon@ss@127.0.0.1:5432/techcamp_live'


class Production(Config):
    pass