from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def survey_result():
	print "Got Post Info"

	name = request.form['name']
	location = request.form['location']
	lang = request.form['lang']
	comment = request.form['comment']
	if(len(name) < 1):
		flash("You must enter a valid name!")
		return redirect('/')
	if(len(comment) > 120):
		flash("Sorry, your comment is more than 120 characters long. Don't do dat!")
		return redirect('/')
		

	return render_template('result.html', info=request.form)

app.run(debug=True)