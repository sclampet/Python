from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['name']) < 1:
		flash("You need to enter a name!")
	else:
	 	flash("LOL Sick name {}".format(request.form['name']))
	return redirect('/')

app.run(debug=True)