from flask import Flask, render_template
import pandas as pd
import sqlite3


app = Flask(__name__)

# this is the default page 
@app.route('/')
def about():
    return render_template('about.html')

# this is the dataset page
@app.route('/data')
def data():
    conn = sqlite3.connect('database/titanic.db')
    cursor = conn.cursor()

    # Execute your SQL query to retrieve data
    execute_data = cursor.execute("SELECT * FROM titanic_table LIMIT 25")
    data = cursor.fetchall()

    conn.close()

    return render_template('data.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True)
