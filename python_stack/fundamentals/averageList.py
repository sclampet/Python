# Print the average of the values in a list

a = [1, 2, 5, 10, 255, 3]

def avgList():
	sum = 0
	for ele in a:
		sum += ele
	print sum / len(a)