# Multiply each list value by 5

a = [2,4,10,16] 

def multiply(a_li, mult):
	for i in range(len(a_li)):
		a_li[i] *= mult
	print a_li
multiply(a,5)
