from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'loginreg')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	return render_template('index.html', title='Login and Registration')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

@app.route('/register/user', methods=['POST'])
def create():
	fn = request.form['first_name']
	ln = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confpass = request.form['conf_password']
	errors = []

	if len(fn) < 1 or len(ln) < 1 or len(email) < 1 or len(password) < 1:
		errors.append('All fields must be filled out correctly!')
	elif not EMAIL_REGEX.match(email):
		errors.append('Must be a valide email address!')
	elif len(fn) < 2 or len(ln) < 2:
		errors.append('Both first and last name must be at least 2 characters long!')
	elif len(password)< 8:
		errors.append('Password must be at least 8 characters long!')
	elif password != confpass:
		errors.append('Passwords do not match!')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/register')
	else:
		flash('Success!')
		pw_hash = bcrypt.generate_password_hash(password)
		query = """INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at)
		VALUES (:fist_name, :last_name, :email, :password, NOW(), NOW())"""
		data = {
			'fist_name': fn,
			'last_name': ln,
			'email': email,
			'password': pw_hash,
		}
		mysql.query_db(query, data)
		return redirect('/register')

@app.route('/users', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	errors = []
	user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	data = {
		'email': email,
	}
	user = mysql.query_db(user_query, data)
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		flash('Successful Login!')
		return redirect('/')
	else:
		flash('Invalid Email!')
		return redirect('/')

	if len(email) < 1 or len(password) < 1:
		errors.append('All fields must be filled out correctly!')
	elif not EMAIL_REGEX.match(email):
		errors.append('Must be a valide email address!')
	elif len(password)< 8:
		errors.append('Password must be at least 8 characters long!')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		flash('Success!')



	return redirect('/')

app.run(debug=True)