from flask import Flask, render_template, url_for, request, flash, session, redirect
from databases import *
from machinelearning import combine_images, main_colour_in_image, remove_background
import os

app = Flask('Stylista')
app.secret_key='fhth5gderdchrdgesxeshxesxesxesx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer1 = request.form["aesthetic"]
        answer2 = request.form["body_type"]
        answer3 = request.form["combination"]
        answer4 = request.form["color"]
        answer5 = request.form["colour"]
        answer6 = request.form["comfort"]
        if get_quiz_results(session["username"]) != False:
            override_quiz_results(answer1, answer2, answer3, answer4, answer5, answer6, session["username"])
        else:
            add_quiz_results(session["username"], answer1, answer2, answer3, answer4, answer5, answer6)
        return redirect(url_for('index'))
    else:
        if "username" in session:
            return render_template('quiz.html')
        else:
            flash("You need to login first!")
            return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if check_login(username, password) == False:
            flash("Your credentials are wrong, please try again!")
            return render_template("login.html")
        else:
            flash("Successful login!")
            session["username"] = username
            return redirect(url_for('index'))
    else:
        return render_template("login.html")
    
@app.route('/signup', methods=['GET', 'POST'])#
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        re_enter_password = request.form["re-enter_password"]
        if password != re_enter_password:
            flash("Your password doesn't match, please try again!")
            return render_template("signup.html")
        if check_username(username):
            flash("This username already exists, please try again!")
            return render_template("signup.html")
        if check_email(email):
            flash("This email already exists, please try again!")
            return render_template("signup.html")
        if check_password(password) != True:
            flash(check_password(password))
            return render_template("signup.html")
        add_user(username, email,  password)
        return redirect(url_for('login'))
    else:
        return render_template("signup.html")
    
@app.route('/wardrobe' , methods=['GET', 'POST'])
def wardrobe():
    return render_template('wardrobe.html')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['upload']
        accepted_extensions = ["png", "jpg", "jpeg", "bmap", "svg"]
        if image.filename.split(".")[-1] not in accepted_extensions:
            flash("This file format is not supported, please try again!")
            return render_template("wardrobe.html")
        image = remove_background(image)
        image_withBG = combine_images(image)
        colour = main_colour_in_image(image_withBG)
        item = check_item(image)
        itemnumber = get_image_amount()
        image.save("static/uploaded_images/" + str(itemnumber) + ".png")
        add_image(session["username"], item, colour)

        


if __name__ == '__main__':
    app.run(debug=True)