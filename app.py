from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sql_injection', methods=["GET", "POST"])
def sql_injection():
    result = ""
    if request.method == "POST":
        user_input = request.form['username']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        try:
            query = f"SELECT * FROM users WHERE username = '{user_input}'"
            cursor.execute(query)
            data = cursor.fetchall()
            result = data if data else "No user found"
        except Exception as e:
            result = str(e)
        conn.close()
    return render_template("sql_injection.html", result=result)

@app.route('/xss', methods=["GET", "POST"])
def xss():
    result = ""
    if request.method == "POST":
        comment = request.form['comment']
        result = comment  # Deliberately unsafe rendering
    return render_template("xss.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)

