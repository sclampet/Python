from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random

@app.route('/')
def index():
	if 'rand' not in session:
		session['rand'] = random.randrange(0,101)
	else:
		pass
	return render_template('index.html', title='Great Number Game')



@app.route('/guess', methods=['POST'])
def user_guess():
	print "Got Post Info"

	session['guess'] = int(request.form['guess'])
	guess = session['guess']		
	

	if(session['guess'] > session['rand']):
		session['result'] = 1
	elif(session['guess'] < session['rand']):
		session['result'] = 0
	else:
		session['result'] = 2

	print 'rand number:', session['rand'], ',', session['result']

	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)


