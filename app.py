from flask import Flask, render_template, url_for, request, flash, session
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
        insert_answer(answer1, answer2, answer3, answer4, answer5, answer6)
        print(answer1, answer2, answer3, answer4, answer5, answer6)
        flash('Your answers have been submitted!')
        return render_template('quiz.html')
    else:
        return render_template('quiz.html')


if __name__ == '__main__':
    app.run(debug=True)