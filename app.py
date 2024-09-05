from flask import Flask, render_template, request
import psycopg2
from psycopg2 import sql
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "vit@123"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['Email_Address']
    password = request.form['Password']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(sql.SQL("SELECT * FROM login WHERE Email_Address = %s"), [email])
    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        stored_password = user[1]  # Password is at index 1

        if stored_password == password:
            return 'Login successful!'
        else:
            return 'Invalid email or password.'
    else:
        return 'Invalid email or password.'

if __name__ == '__main__':
    app.run(debug=True)
