class Car():
	def __init__(self, price, speed, fuel, mileage):
		tax = 0
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def display_all(self):
		print 'Price: ', self.price
		print 'Speed: ', self.speed
		print 'Fuel: ', self.fuel
		print 'Mileage: ', self.mileage
		if self.price > 10000:
			tax = 0.15
			print 'Tax: ', tax
			print '\t'
		else:
			tax = 0.12
			print 'Tax: ', tax
			print '\t'

car1 = Car(2000, '35mph', 'Full', '15mpg')
car1.display_all()

car2 = Car(2000, '5mph', 'Not Full', '105mpg')
car2.display_all()

car3 = Car(2000, '15mph', 'Kind of Full', '95mpg')
car3.display_all()

car4 = Car(2000, '25mph', 'Full', '25mpg')
car4.display_all()

car5 = Car(2000, '45mph', 'Full', '25mpg')
car5.display_all()

car6 = Car(20000000, '35mph', 'Full', '15mpg')
car6.display_all()
