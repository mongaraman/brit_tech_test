from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required
from .models.user import User
from .models.product import Product
from .db import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('main.register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful.')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.products'))
        flash('Invalid username or password.')
        return redirect(url_for('main.login'))
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
    return render_template('summary.html', total_cost=total_cost)
