from app import app, db, Product

def initialize_database():
    with app.app_context():
        db.create_all()

        products = [
            Product(name='Apples', price=5),
            Product(name='Book', price=100),
            Product(name='Car', price=20000)
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()

if __name__ == '__main__':
    initialize_database()