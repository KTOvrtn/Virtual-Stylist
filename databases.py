import sqlite3

def create_table():
    conn = sqlite3.connect('quiz_answers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists answers
                    (answer1 text, answer2 text, answer3 text, answer4 text, answer5 text, answer6 text)''')
    conn.commit()
    conn.close()

def insert_answer(answer1, answer2, answer3, answer4, answer5, answer6):
    conn = sqlite3.connect('quiz_answers.db')
    c = conn.cursor()
    c.execute('''INSERT INTO answers VALUES (?, ?, ?, ?, ?, ?)''', (answer1, answer2, answer3, answer4, answer5, answer6))
    conn.commit()
    conn.close()
    
create_table()