# Populate a sample list with 100 values (where each value is a random number between 0 to 10000). 
# Implement a selection sort algorithm that returns a new list thats sorted 
# (with smallest number on the left). Do this without creating another list.



# Modify your code so that instead of just getting the minimum when doing the linear scan, 
# it gets BOTH the maximum and the minimum and swaps two values after each linear scan.


import random

def selection_sort(a_li):
	minStart = 0
	maxStart = len(a_li) - 1
	while minStart < len(a_li):
		for num in range(minStart, len(a_li) - 1 / 2):
			if a_li[num] < a_li[minStart]:
				a_li[num], a_li[minStart] = a_li[minStart], a_li[num]
		for num in range(maxStart, len(a_li) - 1 / 2, -1):
			if a_li[num] > a_li[maxStart]:
				a_li[num], a_li[maxStart] = a_li[maxStart], a_li[num]
		minStart+=1
	return a_li



list1 = [2,1,4,3,6,5]
list2 = [random.randint(0,10000) for count in range(100)]

print selection_sort(list1)
print selection_sort(list2)