from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt 
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'restful_users')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	#display all users query
	allusers_query = "SELECT * FROM users"
	allusers = mysql.query_db(allusers_query)

	#check if user is logged in and pull info
	#check if user is logged in and pull info
	if 'user_id' not in session or not session['user_id']:
		return render_template('index.html', title='Semi Restful Users', allusers=allusers)
	else:
		user_query = "SELECT first_name, last_name FROM users WHERE id = :id"
		user_data = {'id': session['user_id']}
		user = mysql.query_db(user_query, user_data)
		title = str(user[0]['first_name'])+" "+str(user[0]['last_name'])
		return render_template('index.html', title=title, allusers=allusers, user=user)


	return render_template('index.html', title='Semi Restful Users', users=users, user=user)

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	#errors handler
	errors = []

	#login form validations
	if len(email) < 1 or len(password) < 1:
		errors.append('You must fill in both fields to login')
	elif not EMAIL_REGEX.match(email):
		errors.append('Make sure you entered a valid email')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')

	#check to see if email exists
	query = "SELECT id, pw_hash FROM users WHERE email = :email"
	data = {'email': email}

	try:
		user = mysql.query_db(query,data)
		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
			session['user_id'] = user[0]['id']
			print 'Login Successful'
			return redirect('/')
		else:
			flash('Incorrect password')
			return redirect('/')
	except:
		flash('Email does not exist')
	return redirect('/')

@app.route('/logout')
def logout():
	session['user_id'] = None
	return redirect('/')


@app.route('/register')
def register():
	return render_template('register.html', title='Sign Up')

@app.route('/users', methods=['POST'])
def create_user():
	fn = request.form['first_name']
	ln = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']
	#errors handler
	errors = []

	#check to see if user already exists
	duplication_query = "SELECT id FROM users WHERE email = :email"
	duplication_data = {'email': email}
	duplication_check = mysql.query_db(duplication_query, duplication_data)
	if duplication_check:
		errors.append('This user already exists!')

	#registration from validations
	if len(fn) < 1:
		errors.append('Please fill out a first name')
	elif not fn.isalpha():
		errors.append('Must be a valid first name')

	if len(ln) < 1:
		errors.append('Please fill out a last name')
	elif not ln.isalpha():
		errors.append('Must be a valid last name')

	if len(email) < 1:
		errors.append('Please put an email address')
	elif not EMAIL_REGEX.match(email):
		errors.append('Must be a valid email address')

	if len(password) < 8:
		errors.append('Password must be at least 8 characters long')
	elif password != confirm:
		errors.append('Passwords do not match')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/register')
	else:
		#bcrypt password
		pw_hash = bcrypt.generate_password_hash(password)

		#insert new user query
		query = """INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) 
		VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
		data = {
			'first_name': fn,
			'last_name': ln,
			'email': email,
			'pw_hash': pw_hash,
		}
		user = mysql.query_db(query,data)
		print user
		return redirect('/')

@app.route('/users/new')
def new_user():
	return render_template('new-user.html', title="Add User")

@app.route('/users/create', methods=['POST'])
def create_new_user():
	fn = request.form['first_name']
	ln = request.form['last_name']
	email = request.form['email']
	#errors handler
	errors = []

	#add user validations
	if len(fn) < 1:
		errors.append('Please enter a first name')
	elif not fn.isalpha():
		errors.append('Please enter a valid first name')

	if len(ln) < 1:
		errors.append('Please enter a last name')
	elif not ln.isalpha():
		errors.append('Please enter a valid last name')

	if len(email) < 1:
		errors.append('Please put an email address')
	elif not EMAIL_REGEX.match(email):
		errors.append('Must be a valid email address')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/users/new')
	else:
		#insert new user query
		query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at) 
		VALUES (:first_name, :last_name, :email, NOW(), NOW())"""
		data = {
			'first_name': fn, 
			'last_name': ln, 
			'email': email,
		}
		mysql.query_db(query,data)
	return redirect('/users/<id>')

@app.route('/users/<id>')
def user_profile(id):
	



app.run(debug=True)