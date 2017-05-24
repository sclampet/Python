from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*[&%$]).{6,}$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	dob = request.form['last_name']
	password = request.form['pass']
	conf_pass = request.form['conf_pass']

	if len(email) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(password) < 1 or len(conf_pass) < 1:
		flash('You Must Complete All Fields!')
	elif first_name.isalpha() == False or last_name.isalpha() == False:
		flash("Name Must Contain Only Letters!")
	elif len(password) < 9:
		flash('Password Must Be More Than 8 Characters Long!')
	elif password != conf_pass:
		flash('Passwords Do Not Match!')
	elif not PASS_REGEX.match(password):
		flash('Password Must Contain At Least One Capital Letter and Number!')
	elif not EMAIL_REGEX.match(email):
		flash('Must Be A Valid Email!')
	else:
		flash('Success!')

	return redirect('/')

app.run(debug=True)