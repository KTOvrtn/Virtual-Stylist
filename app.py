from flask import Flask, render_template, url_for, request, flash, session, redirect
from databases import *

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
        add_quiz_results(session["username"], answer1, answer2, answer3, answer4, answer5, answer6)
        print(answer1, answer2, answer3, answer4, answer5, answer6)
        flash('Your answers have been submitted!')
        return render_template('quiz.html')
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
            return render_template('index.html')
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)