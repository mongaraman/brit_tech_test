from flask import Flask
from flask_migrate import Migrate
from app import create_app, db
from app.utils import initialize_database


app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        initialize_database()
