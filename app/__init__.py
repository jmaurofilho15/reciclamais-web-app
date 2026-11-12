import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-secreta-reciclamais-mvp')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reciclamais.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from app import models, routes
        db.create_all()

    return app