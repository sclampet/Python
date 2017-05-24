# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display 
# how many times the head/tail appears.

import random

def coin_tosses(num_tosses):
	print "Starting the program..."
	heads = 0
	tails = 0
	for num in range(num_tosses):
		result = int(round(random.random())
		print result
		if(result is 1):
			current = "heads!"
			heads += 1
		else:
			current = "tails!"
			tails += 1
		print "Attempt #" + str(num + 1) + " Throwing a coin... It's " + str(current) + " Got " + str(heads) + " heads(s) so far and " + str(tails) + " tails(s) so far."
	print "Ending the program, thank you!"
coin_tosses(5000)