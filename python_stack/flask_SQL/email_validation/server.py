from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success')
def success():
	flash('Email added!', 'success')
	query = "SELECT * FROM email_users"
	emails = mysql.query_db(query)

	return render_template('success.html', emails=emails)

@app.route('/add-email', methods=['POST'])
def add_email():
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Not a Valid Email!', 'errors')
		return redirect('/')
	else:
		query = """INSERT INTO email_users (email, created_at, updated_at)
		VALUES (:email, NOW(), NOW())"""
		data = {
			'email': request.form['email']
		}
		mysql.query_db(query, data)
		return redirect('/success')

@app.route('/delete/<id>')
def delete(id):
	query = "DELETE FROM email_users WHERE id = :id"
	data = {
		'id': id,
	}
	mysql.query_db(query, data)

	return redirect('/success')

app.run(debug=True)