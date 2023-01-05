from flask import redirect, url_for, render_template, request, flash, session
from . import main
from .models import User, hash_password
from flask_login import login_user, current_user, login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        passwordConfirm = request.form['confirm-password']
        if password != passwordConfirm:
            message = 'Passwords do not match'
            flash(message)
            return redirect(url_for('main.index'))
        password = hash_password(password)
        if User(username, email, password).store_user():
            message = 'Registration successful'
        else:
            message = 'Registration failed, please try again'
        flash(message)
        return redirect(url_for('main.index'))


@main.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        userClass = User(username, None, password)
        user = userClass.get_user()
        if user:
            if userClass.hash_check(password):
                message = 'Incorrect password'
                flash(message)
                return redirect(url_for('main.index'))
            message = 'Login successful'
            login_user(user)
        else:
            message = 'Incorrect username or password'
        flash(message)
        return redirect(url_for('main.index'))


@main.route('/profile', methods=['GET', 'POST'])
def profile():
    print(current_user)
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        passwordConfirm = request.form['confirm-password']
        if password != passwordConfirm:
            message = 'Passwords do not match'
            flash(message)
            return redirect(url_for('main.profile'))
        password = hash_password(password)
        if User(session['username'], email, password).update_user(
                {'username': username, 'email': email, 'password': password}):
            message = 'Profile updated'
            session['username'] = username
            session['email'] = email
        else:
            message = 'Profile update failed, please try again'
        flash(message)
        return redirect(url_for('main.profile'))
    return render_template('chat.html')
# @main.route('/chat')
# def chat():
#     """Chat room. The user's name and room must be stored in
#     the session."""
#     name = session.get('name', '')
#     room = session.get('room', '')
#     if name == '' or room == '':
#         return redirect(url_for('.index'))
#     return render_template('chat.html', name=name, room=room)
