# encoding=utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_ext(app):
    db.init_app(app)
    db.app = app
    db.create_all()
