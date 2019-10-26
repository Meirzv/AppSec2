import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.urandom(32) or "meir-zeevi"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meir.db'
