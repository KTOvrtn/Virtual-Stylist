from flask import Flask, render_template, url_for

app = Flask('Stylista')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)