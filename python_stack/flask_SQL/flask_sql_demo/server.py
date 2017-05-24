from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app, 'world')

@app.route('/')
def index():
	result = mysql.query_db('SELECT * FROM cities LIMIT 10')
	return render_template('index.html', result=result)

app.run(debug=True)