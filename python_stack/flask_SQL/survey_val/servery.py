from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'students')
bcrypt = Bcrypt(app)

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\-]+$')



@app.route('/')
def index():
	query = "SELECT * FROM users"
	students = mysql.query_db(query)
	return render_template('index.html', title='Student Survey', students=students)

@app.route('/users', methods=['POST'])
def create():
	fn = request.form['first_name']
	ln = request.form['last_name']
	bday = request.form['birth_date']
	password = request.form['password']
	confirm = request.form['conf_password']

	errors = []

	if len(request.form['first_name']) < 2:
		errors.append('First name must be longer than 2 characters.')
	elif not NAME_REGEX.match(request.form['first_name']):
		errors.append('First name cannot contain special characters or numbers!')

	if len(request.form['last_name']) < 2:
		errors.append('Last name must be longer than 2 characters.')
	elif not NAME_REGEX.match(request.form['last_name']):
		errors.append('Last name cannot contain special characters or numbers!')

	if len(password) < 8:
		errors.append('Password must be at least 8 characters long')
	elif password != confirm:
		errors.append('Passwords do not match')	

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		flash('Fuck yeah, you did it!!')
		pw_hash = bcrypt.generate_password_hash(password)
		data = {
			'first_name': fn,
			'last_name': ln,
			'birth_date': bday,
			'password': pw_hash, 
		}
		print data
		mysql.query_db(data)
		return redirect('/')

app.run(debug=True)