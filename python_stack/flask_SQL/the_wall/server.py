from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'thewall')
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	#messages query
	messages_query = """SELECT messages.id, messages.message, messages.created_at,
	users_id AS user_id, users.first_name, users.last_name FROM messages
		JOIN users ON messages.users_id = users.id
		ORDER BY messages.created_at DESC"""
	#run message query
	messages = mysql.query_db(messages_query)

	#comments query
	comment_query = """SELECT comments.id,
		comments.comment,
		comments.created_at,
		messages.id AS message_id,
		users.id AS user_id,
		users.first_name,
		users.last_name FROM comments
			JOIN users ON comments.users_id = users.id
			JOIN messages ON comments.messages_id = messages.id
			ORDER BY comments.created_at ASC"""
	comments = mysql.query_db(comment_query)

	#check if user is logged in and pull info
	if 'user_id' not in session or not session['user_id']:
		return render_template('index.html', title='The Wall', messages=messages, comments=comments)
	else:
		user_query = "SELECT first_name, last_name FROM users WHERE id = :id"
		user_data = {'id': session['user_id']}
		user = mysql.query_db(user_query,user_data)
		title = str(user[0]['first_name'])+" "+str(user[0]['last_name'])
		return render_template('index.html', user=user, title=title, messages=messages, comments=comments)

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/users', methods=['POST'])
def create_user():
	#create variables to save time
	fn = request.form['first_name']
	ln = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']
	errors = []

	#check to see if email provided in reg. already exists in db
	duplication_query = "SELECT email FROM users WHERE email = :email"
	duplication_data = {'email' : email}
	duplication_check = mysql.query_db(duplication_query, duplication_data)
	if duplication_check:
		errors.append('A user already exists with that email')

	if len(fn) < 1:
		errors.append('Please enter a first name')
	elif not fn.isalpha():
		errors.append('Must be a valid first name')

	if len(ln) < 1:
		errors.append('Please enter a last name')
	elif not ln.isalpha():
		errors.append('Must be a valid last name')

	if len(email) < 1:
		errors.append('Please provide an email address')
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
		#encrypt password
		pw_hash = bcrypt.generate_password_hash(password)

		user_query = """INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at)
		VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
		user_data = {
			'first_name': fn,
			'last_name': ln,
			'email': email, 
			'pw_hash': pw_hash
		}
		new_user = mysql.query_db(user_query, user_data)
		print new_user
		return redirect('/')

@app.route('/login', methods=['POST']) #log in user
def login():
	email = request.form['email']
	password = request.form['password']
	errors = []

	#form validations
	if len(email) < 1 or len(password) < 1:
		errors.append('You must fill out both fields to login')
	elif not EMAIL_REGEX.match(email):
		errors.append('Must enter a valid email address')

	#flash error messages, if any
	if errors:
		for error in errors:
			flash(error)
		return redirect('/')

	#check to see if user already exists
	query = "SELECT id, pw_hash FROM users WHERE email = :email"
	data = {'email': email}

	try:
		user = mysql.query_db(query, data)
		print user
		#check password
		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
			session['user_id'] = user[0]['id']
			print 'Successful login'
			return redirect('/')
		else:
			flash('Incorrect password')
			return redirect('/')
	except:
		flash('No user found with that email address')
	return redirect('/')

@app.route('/logout')
def logout():
	session['user_id'] = None;
	return redirect('/')

@app.route('/messages', methods=['POST'])
def create_message():
	message = request.form['message']
	errors = []

	#message validations
	if len(message) < 1:
		errors.append('Cannot post a blank message!')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		#run insert message query
		query = "INSERT INTO messages(message, created_at, updated_at, users_id) VALUES(:message, NOW(), NOW(), :users_id)"
		data = {
			'message': message,
			'users_id': session['user_id']
		}
		mysql.query_db(query,data)
	return redirect('/')

@app.route('/comments', methods=['POST'])
def comment():
	message_id = request.form['message-id']
	comment = request.form['comment']
	#errors handler
	errors = []

	#comment validations
	if len(comment) < 1:
		errors.append('Cannot post a blank message')

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		#insert comment query
		query = """INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) 
		VALUES (:comment, NOW(), NOW(), :users_id, :messages_id)"""
		data = {
			'comment': comment,
			'users_id': session['user_id'],
			'messages_id': message_id
		}
		mysql.query_db(query,data)
	return redirect('/')


@app.route('/messages/<id>/delete', methods=['POST'])
def destroy_message(id):
	#run delete message query
	message_query = "DELETE FROM messages WHERE id = :id"
	message_data = {'id': id}
	mysql.query_db(message_query,message_data)

	#run delete comment query
	comment_query = "DELETE FROM comments WHERE messages_id = :id"
	mysql.query_db(comment_query,message_data)

	return redirect('/')

@app.route('/comments/<id>/delete', methods=['POST'])
def destory_comment(id):
	#delete comment query
	query = "DELETE FROM comments WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query,data)

	return redirect('/')


app.run(debug=True)