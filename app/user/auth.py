from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
from demo.app.user.forms import LoginForm, RegisterForm
from demo import bcrypt
from .models import User
from demo import db
from flask_login import login_user, current_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(meta={'locales': ['zh']})

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(meta={'locales': ['zh']})
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            print(1)
            login_user(user, remember=form.remember.data)
            flash('Login successful', 'danger')
            return redirect(url_for('main.index'))
        else:
            print(2)
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout successful.', 'danger')
    return redirect(url_for('main.index'))
