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
    
@app.route('/items/<clothing_type>', methods=['GET', 'POST'])
def items_viewer(clothing_type):
    if "username" in session:
        items = query_images(session["username"], clothing_type)
        listofnumbers = []
        for item in items:
            listofnumbers.append(str(item[0]))

        if items != "[]":
            return render_template("wardrobe.html", items=listofnumbers, show_popup = True)
        else:
            return render_template("wardrobe.html", items="No items found", show_popup = False)
    else:
        flash("You need to login first!")
        return redirect(url_for('login'))
   
    
@app.route('/wardrobe' , methods=['GET', 'POST'])
def wardrobe():
    if "username" in session:
        return render_template("wardrobe.html", show_popup = False)
    else:
        flash("You need to login first!")
        return redirect(url_for('login'))


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        clothing_type = request.form["clothing_type"]
        image = request.files['upload']
        accepted_extensions = ["png", "jpg", "jpeg", "bmap", "svg"]
        if image.filename.split(".")[-1] not in accepted_extensions:
            flash("This file format is not supported, please try again!")
            return render_template("wardrobe.html")
        itemnumber = get_image_amount()
        remove_background(image, itemnumber)
        combine_images()
        colour = main_colour_in_image("static/uploaded_images/temporaryimages/mergedimage.png")
        add_image(session["username"], clothing_type, colour)

    flash("Upload Success")
    return render_template('wardrobe.html')

if __name__ == '__main__':
    app.run(debug=True)