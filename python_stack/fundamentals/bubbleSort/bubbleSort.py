
import random

a_li = [6,5,3,1,8,7,2,4]

def bubble_sort(a_li):
	swapped = True
	while(swapped):
		swapped = False
		for i in range(len(a_li) - 1):
			if(a_li[i] > a_li[i + 1]):
				a_li[i], a_li[i + 1] = a_li[i + 1], a_li[i]
				swapped = True
	print a_li

random_list = [random.randint(0,10000) for count in range(100)]
bubble_sort(a_li)
print bubble_sort(random_list)

