from flask_sqlalchemy import SQLAlchemy
from flask import g

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def get_db():
    if 'db' not in g:
        g.db = db
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.session.close()