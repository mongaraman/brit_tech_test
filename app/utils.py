# app/utils.py
from app import db, Product, User
from flask import current_app

def initialize_database():
    with current_app.app_context():
        # Create all tables
        db.create_all()

        # Add initial users
        users = [
            {'username': 'user1', 'password': 'password1'},
            {'username': 'user2', 'password': 'password2'}
        ]
        # Add initial users
        products = [
            User(username='user1', password='password1'),
            Product(name='Book', price=100),
            Product(name='Car', price=20000)
        ]


        for user_data in users:
            username = user_data['username']
            password = user_data['password']
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)

        # Add initial products
        products = [
            Product(name='Apples', price=5),
            Product(name='Book', price=100),
            Product(name='Car', price=20000)
        ]

        # Bulk insert products
        db.session.bulk_save_objects(products)
        db.session.bulk_save_objects(users)
        db.session.commit()

        print("Initialization complete: Users and Products added successfully.")
        

if __name__ == '__main__':
    initialize_database()