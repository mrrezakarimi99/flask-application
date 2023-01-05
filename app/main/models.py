import pymysql.cursors
import hashlib

from flask_login import UserMixin

connection = pymysql.connect(
    host='localhost',
    user='admin',
    password='admin!!!',
    db='app_test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_user(username):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', username)
    user = cursor.fetchone()
    cursor.close()
    if user:
        return True
    return False


class User(UserMixin):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def get_user(self, username=None):
        if username is None:
            username = self.username
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', username)
        user = cursor.fetchone()
        cursor.close()
        return user

    def store_user(self):
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                       (self.username, self.email, self.password))
        connection.commit()
        cursor.close()
        return True

    def update_user(self, data):
        cursor = connection.cursor()
        cursor.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE username = %s',
                       (data['username'], data['email'], data['password'], self.username))
        connection.commit()
        cursor.close()
        return True

    def delete_user(self):
        cursor = connection.cursor()
        cursor.execute('DELETE FROM users WHERE username = %s', self.username)
        connection.commit()
        cursor.close()
        return True

    def hash_check(self, password):
        if self.password == hash_password(password):
            return True
        return False

    def get_by_id(self, user_id):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', user_id)
        user = cursor.fetchone()
        cursor.close()
        return user

