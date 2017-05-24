# Given the following list:

students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def full_name(a_li):
	for student in students:
		print student['first_name'], student['last_name']

full_name(students)	
