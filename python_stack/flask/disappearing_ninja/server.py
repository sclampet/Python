from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return 'No Ninjas Here'

@app.route('/ninjas')
def ninjas():
	return render_template('index.html', allNinjas=True)

@app.route('/ninjas/<ninja_color>')
def show_ninja(ninja_color):
	return render_template('index.html', color=ninja_color, allNinjas=False)

app.run(debug=True)