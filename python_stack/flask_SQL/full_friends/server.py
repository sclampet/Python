from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
	query = 'SELECT * FROM users'
	friends = mysql.query_db(query)
	return render_template('index.html', title='Full Friends', friends=friends)

@app.route('/add-friend', methods=['POST'])
def create():
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Please enter a valid email!')
		return redirect('/')
	elif len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1:
		flash('Must fill out all fields!')
		return redirect('/')
	else:
		query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at)
		VALUES (:first_name, :last_name, :email, NOW(), NOW())"""
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
		}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM users WHERE id = :id"
	data = {
		'id': id,
	}
	friend = mysql.query_db(query, data)
	return render_template('friends.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	query = """UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, 
	updated_at = NOW() WHERE id = :id"""
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'id': request.form['id'],
	}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
	query = "DELETE FROM users WHERE id = :id"
	data = {
		'id':id,
	}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)