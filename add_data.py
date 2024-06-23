# app/add_data.py

from app import create_app, db
from app.models.user import User
from app.models.product import Product

app = create_app()

# Example data
users_data = [
    {'username': 'rmn1', 'password': 'testpass1'},
    {'username': 'rmn2', 'password': 'testpass2'}
]

products_data = [
    {'name': 'Apples', 'price': 5.0},
    {'name': 'Book', 'price': 100.0},
    {'name': 'Car', 'price': 20000.0}
]

# Function to add users
def add_users():
    for data in users_data:
        username = data['username']
        password = data['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
    db.session.commit()

# Function to add products
def add_products():
    for data in products_data:
        name = data['name']
        price = data['price']
        product = Product(name=name, price=price)
        db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        add_users()
        add_products()
