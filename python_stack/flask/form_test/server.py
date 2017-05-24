from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/') #used to render our form
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST']) # this route will handle our form submission
def create_users(): # notice how we defined which HTTP methods are allowed by this route
	print "Get Post Info"

	session['name'] = request.form['name']
	session['email'] = request.form['email']

	return redirect('/show')
@app.route('/show')
def show_user():
	return render_template('user.html')

app.run(debug=True) #runs our server