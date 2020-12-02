from flask import render_template, request, jsonify, flash, url_for, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from chiblog.User.user_model import User

user = Blueprint('user', __name__)

@user.route('/admin', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if request.method=='POST':
        email = request.form['email']
        print(email)
        password = request.form['password']
        user = User.query.filter_by(email = email).first()
        print(user.password)
        #if user and check_password_hash(user.password, password):
        if user and user.password == password:
            login_user(user)
            print('Logged in')
            next_page = request.args.get('next')
            flash('Welcome back Chi', "dark")
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            print('Fail')
            flash('Login Unsuccessful bruh :<', "danger")
    return render_template('login.html', title='Login admin')

@user.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))



