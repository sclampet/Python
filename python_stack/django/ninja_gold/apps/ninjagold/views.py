from django.shortcuts import render, redirect

import random
import datetime

# Create your views here.
def index(request):
	#set counter to 0 if new session
	if 'count' not in request.session:
		request.session['count'] = 0
	else:
		pass

	#for displaying activities
	if 'action' not in request.session:
		request.session['action'] = []

	context = {
		'count': request.session['count'],
		'action': request.session['action']
	}

	return render(request, 'ninjagold/index.html', context)

def process(request):
	request.session['building'] = request.POST['building']
	building = request.session['building']

	#reset counter and activities list
	if building == 'reset':
		request.session['count'] = 0
		request.session['action'] = []

	#check which form
	if building == 'farm':
		farm_gold = int(random.randrange(10,21))
		request.session['count'] += farm_gold
		addAction(request, farm_gold, 'earned', 'farm')
		print farm_gold

	if building == 'cave':
		cave_gold = int(random.randrange(5,11))
		request.session['count'] += cave_gold
		addAction(request, cave_gold, 'earned', 'cave')
		print cave_gold

	if building == 'house':
		house_gold = int(random.randrange(2,6))
		request.session['count'] += house_gold
		addAction(request, house_gold, 'earned', 'house')
		print house_gold

	if building == 'casino':
		casino_gold = int(random.randrange(-50,51))
		request.session['count'] += casino_gold
		if casino_gold < 0:
			addAction(request, casino_gold, 'lost', 'casino')
		else:
			addAction(request, casino_gold, 'earned', 'casino')

		print casino_gold

	return redirect('/')

def addAction(request, num, action, place):
	#to display proper current date format
	timestamp = datetime.datetime.now()

	#insert relative activity info into action list
	if place == 'farm':
		request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
	if place == 'cave':
		request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
	if place == 'house':
		request.session['action'].insert(0,['earn', 'Earned %d from the %s! %s' % (num, place, timestamp)])
	if place == 'casino':
		if action == 'earned':
			earned = 'Earned %d from the casino! %s' % (num, timestamp)
			request.session['action'].insert(0,['earn', earned])
		elif action == 'lost':
			lost = 'Entered the casino and lost %d gold... Ouch %s' % (num, timestamp)
			request.session['action'].insert(0,['lost', lost])
	else:
		print "error"

	return redirect('/')

