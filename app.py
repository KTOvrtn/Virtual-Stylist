from flask import Flask, render_template, url_for, request, flash, session, redirect
from databases import *
from machinelearning import combine_images, main_colour_in_image, remove_background
from outfitgen import generating_outfits_without_quizans, generating_outfits_with_quizans
import os
import pyttsx3
import threading
import speech_recognition as sr

app = Flask('Stilista')
app.secret_key='fhth5gderdchrdgesxeshxesxesxesx'

@app.route('/')
def index():
    if "volume" in session:
        if session["volume"] == True:
            threading.Thread(target=SpeechOutput, args=("Welcome to Stilista, your personal stylist!",)).start()
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
            delete_quiz_results(session["username"])
            add_quiz_results(session["username"], answer1, answer2, answer3, answer4, answer5, answer6)
        else:
            add_quiz_results(session["username"], answer1, answer2, answer3, answer4, answer5, answer6)
        return redirect(url_for('index'))
    else:
        if "username" in session:
            if "volume" in session:
                if session["volume"] == True:
                    threading.Thread(target=SpeechOutput, args=("Welcome to the quiz, here the website will learn about your style and personality in order to create outfits unique to you.",)).start()
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
        if "volume" in session:
            if session["volume"] == True:
                threading.Thread(target=SpeechOutput, args=("You are required to login.",)).start()
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
        if "volume" in session:
            if session["volume"] == True:
                threading.Thread(target=SpeechOutput, args=("In order to use Stilista you are required to have an account so please signup or if you already have one, login",)).start()
        return render_template("signup.html")
    
@app.route('/items/<clothing_type>', methods=['GET', 'POST'])
def items_viewer(clothing_type):
    if "username" in session:
        if "volume" in session:
            if session["volume"] == True:
                threading.Thread(target=SpeechOutput, args=(f"Here are all of your {clothing_type}",)).start()
        items = query_images(session["username"], clothing_type)
        listofitems = []
        for item in items:
            listofitems.append(str(item[0]))

        if items != "[]":
            return render_template("wardrobe.html", items=listofitems, show_popup = True, clothing_type = clothing_type)
        else:
            return render_template("wardrobe.html", items="No items found", show_popup = False, clothing_type = clothing_type)
    else:
        flash("You need to login first!")
        return redirect(url_for('login'))
    
@app.route('/delete_item/<image_id>', methods=['GET', 'POST'])
def delete_item(image_id):
    if "username" in session:
        username = session["username"]
        if username_imageid_sync(image_id, username) == False:
            return redirect(url_for('wardrobe'))
        else:
            delete_image(image_id)
            return redirect(url_for('wardrobe'))
    else:
        flash("You need to login first!")
        return redirect(url_for('login'))
   
    
@app.route('/wardrobe' , methods=['GET', 'POST'])
def wardrobe():
    if "username" in session:
        if "volume" in session:
            if session["volume"] == True:
                threading.Thread(target=SpeechOutput, args=("Welcome to your virtual wardrobe, here you will be able to upload all your items of clothing in order for Stilista to generate outfits. ",)).start()
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
        itemnumber = get_most_recent_image()
        remove_background(image, itemnumber)
        combine_images()
        colour = main_colour_in_image("static/uploaded_images/temporaryimages/mergedimage.png")
        add_image(session["username"], clothing_type, colour)
    flash("Upload Success")
    if "volume" in session:
            if session["volume"] == True:
                threading.Thread(target=SpeechOutput, args=("Upload successful.",)).start()
    return render_template('wardrobe.html')

@app.route('/generate_outfit', methods=['GET','POST'])
def generate_outfit():
    if request.method == 'POST':
        username = session["username"]
        quiz_results = get_quiz_results(username)
        prompt = request.form["prompt"]
        check_last_question = quiz_results[0][6]
        if check_last_question == "Yes":
            check_bodytype = quiz_results[0][2]
            check_colour = quiz_results[0][5]
            check_average_combination = quiz_results[0][3]
            check_style = quiz_results[0][1]
            outfit = generating_outfits_with_quizans(username, check_bodytype, check_colour, check_average_combination, check_style, prompt)
        else:
            outfit = generating_outfits_without_quizans(username, prompt)
        return render_template("wardrobe.html", outfit = outfit)

@app.route('/toggle_volume/<page>')
def toggle_volume(page):
    if "volume" in session:
        if session["volume"] == True:
            session["volume"] = False
        else:
            session["volume"] = True
    else:
        session["volume"] = True
    return render_template(f"{page}.html")

def SpeechOutput(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    app.run(debug=True)
