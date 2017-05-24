class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		print '\t'
		print "New Bike!"

		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def display_info(self):
		print 'Price:', self.price
		print 'Max Speed:', self.max_speed
		print 'Miles:', self.miles
		return self
	def ride(self):
		print 'Riding...'
		self.miles += 10
		# print 'Total miles:', self.miles
		return self
	def reverse(self):
		print 'Reversing...'
		if self.miles >= 5:
			self.miles -= 5
		else:
			self.miles = 0
		# print 'Total miles', self.miles
		return self

bike1 = Bike(200, '25mph')
bike1.ride().ride().ride().reverse().display_info()

bike2 = Bike(100, '20mph')
bike2.ride().ride().reverse().reverse().display_info()

bike3 = Bike(200, '25mph')
bike3.reverse().reverse().reverse().display_info()


