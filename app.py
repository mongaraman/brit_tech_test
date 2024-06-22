from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://u13ti94r9mo630:p1ed07f3009a05b119f6f5bb4bd805b5e70bfc3f68351e3b1b2478c0d1ddb9c40@c7u1tn6bvvsodf.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d8t2a4i64crn6m'
db = SQLAlchemy(app)

from models import User, Product

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'Registration successful'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('products'))
        return 'Login failed'
    return render_template('login.html')

@app.route('/products')
def products():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('summary.html')

@app.route('/summary')
def summary():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    products = Product.query.all()
    total_cost = sum([product.price for product in products])
    return f'Total cost: £{total_cost}'

if __name__ == '__main__':
    app.run(debug=True)
