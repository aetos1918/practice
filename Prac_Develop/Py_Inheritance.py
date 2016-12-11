class Hack:

	def got(self):
		print("Hacker Online")

	def tat(self):
		print("Go for it.")

class Online(Hack):

	def inhet(self):
		super(Online, self).got()
		print("Child")

a = Online()

a.inhet()

# Lambda Function
from functools import reduce

a = range(1,21)

b = filter(lambda x: x%2 == 0, a) # 2,4,6....
c = reduce(lambda x,y: x+y, a) # 210
d = map(lambda x: x**2, a) # 1,4,9,16.....

