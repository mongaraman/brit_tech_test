from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    #bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'main.login'

    #from .models import user, product

    with app.app_context():
        db.create_all()

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
