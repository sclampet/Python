class MathDojo(object):
	def __init__(self):
		self.total = 0

	def add(self, *num):
		for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]:
					self.total += j
			else:
				self.total += num[i]
		# print self.total
		return self

	def subtract(self, *num):
		for i in range(0, len(num)):
			if type(num[i] is list or type(num[i]) is tuple):
				for j in num[i]:
					self.total -= j
			else:
				self.total -= num[i]
		print self.total
		return self

md = MathDojo()
md.add([1,4]).subtract([1])