from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

import random
import datetime

def addActivity(num, action, place):
    timestamp = datetime.datetime.now()
    if place == 'farm':
        session['activity'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
    elif place == 'cave':
        session['activity'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
    elif place == 'house':
        session['activity'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
    elif place == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            session['activity'].insert(0,['earn', earned])
        elif action == 'lost':
            lost = 'Entered the casino and lost %d gold... Ouch %s' % (num, timestamp)
            session['activity'].insert(0,['lost', lost])
        else:
            print "error"

@app.route('/')
def index():
	if 'counter' not in session:
		session['counter'] = 0
	else:
		pass
	if 'activity' not in session:
		session['activity'] = []
	return render_template('index.html', title='Ninja Gold', activities=session['activity'])

@app.route('/process_money', methods=['POST'])
def find_gold():
	print "Got Post Info"

	if request.form['action'] == 'farm':
		farm_gold = int(random.randrange(10,21))
		session['counter'] += farm_gold
		addActivity(farm_gold, 'earned', 'farm')
		print farm_gold
	elif request.form['action'] == 'cave':
		cave_gold = int(random.randrange(5,11))
		session['counter'] += cave_gold
		addActivity(cave_gold, 'earned', 'cave')
		print cave_gold
	elif request.form['action'] == 'house':
		house_gold = int(random.randrange(2,6))
		session['counter'] += house_gold
		addActivity(house_gold, 'earned', 'house')
		print house_gold
	elif request.form['action'] == 'casino':
		casino_gold = int(random.randrange(-51,51))
		session['counter'] += casino_gold
		if casino_gold < 0:
			addActivity(casino_gold, 'lost', 'casino')
		else:
			addActivity(casino_gold, 'earned', 'casino')
		print casino_gold	

	print session['counter']

	return redirect('/')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)