class Config(object):
    SQLALCHEMY_TRACK_NOTIFICATIO = False


class Development(Config):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@127.0.0.1:5432/ims'