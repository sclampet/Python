from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

@app.route('/users/<username>')
def show_user(username):
	return render_template('user.html', username=username)

app.run(debug=True)