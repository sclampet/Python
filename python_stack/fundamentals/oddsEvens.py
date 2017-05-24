
def odds_evens():
	for number in range(1,2000 + 1):
		if number % 2 == 0:
			print "Number is " + str(number) + ". This is an even number."
		else:
			print "Number is " + str(number) + ". This is an odd number."
odds_evens()