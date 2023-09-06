import sqlite3
import hashlib


def create_user_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,email TEXT,password TEXT)")
    connection.commit()

def add_user(username, email, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",(username, email, hash_password(password)))
    connection.commit()

def hash_password(password):
    hashed_password = hashlib.sha512(password.encode()).hexdigest() #https://docs.python.org/3/library/hashlib.html
    return hashed_password

def check_username(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?",(username,))
    users_the_same = cursor.fetchall()
    if users_the_same:
        return True
    else:
        return False

def check_email(email):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    email_the_same = cursor.fetchall()
    if email_the_same:
        return True
    else:
        return False

def check_login(username, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username, hash_password(password)))
    login_the_same = cursor.fetchall()
    if login_the_same:
        return username
    else:
        return False

def create_quiz_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS quiz (username TEXT PRIMARY KEY , answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT, answer5 TEXT, answer6 TEXT)")
    connection.commit()

def add_quiz_results(username, answer1, answer2, answer3, answer4, answer5, answer6):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO quiz (username, answer1, answer2, answer3, answer4, answer5, answer6) VALUES (?, ?, ?, ?, ?, ?, ?)",(username, answer1, answer2, answer3, answer4, answer5, answer6))
    connection.commit()

def get_quiz_results(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quiz WHERE username=?",(username,))
    quiz_results = cursor.fetchall()
    if quiz_results:
        return quiz_results
    else:
        return False

create_quiz_table()
create_user_table()