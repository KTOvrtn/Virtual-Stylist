import sqlite3
import hashlib
import re


def create_user_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,email TEXT,password TEXT)")
    connection.commit()
    connection.close()

def add_user(username, email, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",(username, email, hash_password(password)))
    connection.commit()
    connection.close()

def hash_password(password):
    hashed_password = hashlib.sha512(password.encode()).hexdigest() #https://docs.python.org/3/library/hashlib.html
    return hashed_password

def check_username(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?",(username,))
    users_the_same = cursor.fetchall()
    connection.close()
    if users_the_same:
        return True
    else:
        return False

def check_email(email):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    email_the_same = cursor.fetchall()
    connection.close()
    if email_the_same:
        return True
    else:
        return False

def check_login(username, password):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username, hash_password(password)))
    login_the_same = cursor.fetchall()
    connection.close()
    if login_the_same:
        return username
    else:
        return False
    
def check_password(password):
    if len(password) <= 7:
        return ("Your password must be 8 characters long!")
    # https://stackoverflow.com/questions/64523621/how-can-i-identify-if-there-is-at-least-one-capital-letter-in-python
    if not (any(x.isupper() for x in password)):
        return ("Your password must contain a capital letter!")
    if not(any(x.isdigit() for x in password)):
        return ("Your password must contain a number!")
    # https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (special_characters.search(password) == None):
        return ("Your password must contain a symbol!")
    return True


def create_quiz_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS quiz (username TEXT PRIMARY KEY , answer1 TEXT, answer2 TEXT, answer3 TEXT, answer4 TEXT, answer5 TEXT, answer6 TEXT)")
    connection.commit()
    connection.close()

def add_quiz_results(username, answer1, answer2, answer3, answer4, answer5, answer6):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO quiz (username, answer1, answer2, answer3, answer4, answer5, answer6) VALUES (?, ?, ?, ?, ?, ?, ?)",(username, answer1, answer2, answer3, answer4, answer5, answer6))
    connection.commit()
    connection.close()

def get_quiz_results(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM quiz WHERE username=?",(username,))
    quiz_results = cursor.fetchall()
    connection.close()
    if quiz_results:
        return quiz_results
    else:
        return False
    
def override_quiz_results(username, answer1, answer2, answer3, answer4, answer5, answer6):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE quiz SET answer1=?, answer2=?, answer3=?, answer4=?, answer5=?, answer6=? WHERE username=?",(answer1, answer2, answer3, answer4, answer5, answer6, username))
    connection.commit()
    connection.close()

def create_image_table():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS images (image_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,item TEXT,colour TEXT)")
    connection.commit()
    connection.close()

def add_image(username, item, colour):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO images (username, item, colour) VALUES (?, ?, ?)",(username, item, colour))
    connection.commit()
    connection.close()

def get_images(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM images WHERE username=?",(username,))
    images = cursor.fetchall()
    connection.close()
    if images:
        return images
    else:
        return False

def get_image_amount():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM images")
    image_amount = cursor.fetchall()
    connection.close()
    return image_amount[0][0]


create_quiz_table()
create_user_table()
create_image_table()