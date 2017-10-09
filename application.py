import flask
import os
from flask_sqlalchemy import SQLAlchemy

application = flask.Flask(__name__)

application.config.from_object(__name__)

DATABASE=os.getenv('database') or 'polrater',
SECRET_KEY=os.getenv('secret_key') or 'development_key',
USERNAME=os.getenv('username') or 'cranklogic',
PASSWORD=os.getenv('password') or 'cranklogic',
HOSTNAME=os.getenv('hostname') or '127.0.0.1',
PORT=os.getenv('port') or '3306'

def generate_db_uri(username, password, hostname, port, db_name):
    return 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
        username,
        password,
        hostname,
        port,
        db_name
    )

application.config.update(dict(
    SQLALCHEMY_DATABASE_URI=generate_db_uri(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
))

db = SQLAlchemy(application)
