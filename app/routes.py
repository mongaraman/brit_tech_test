from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from .models.user import User
from .models.product import Product
from .db import db
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

main_bp = Blueprint('main', __name__)
bcrypt = Bcrypt()

@app.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.products'))
        flash('Login unsuccessful', 'danger')
    return render_template('login.html')

@main_bp.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@main_bp.route('/summary')
@login_required
def summary():
    products = Product.query.all()
    total_cost = sum(product.price for product in products)
    return jsonify({'total_cost': total_cost})
