from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"



@app.route('/')
def index():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1
	return render_template('index.html', title="Counter", counter=session['counter'])


@app.route('/reset')
def reset():
	session['counter'] = 0
	return redirect('/')

@app.route('/add_two')
def add_two():
	session['counter'] += 1
	return redirect('/')

app.run(debug=True)