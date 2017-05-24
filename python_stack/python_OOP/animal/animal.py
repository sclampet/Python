class Animal(object):
	def __init__(self, name):
		self.name = str(name)
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print 'Animal Name: ', self.name
		print 'Health: ', self.health
		return self

jax = Animal('jax')
jax.walk().walk().walk().run().run().displayHealth()

