def add(a,b):
	return a+b

def difference(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b

def modu(a,b):
	return a%b

def big(a,b):
	if a>b:
		return a
	elif a<b:
		return b
	else:
		return "equal"

print(add(45, 29))
print(big(34, 25))
print(difference(34, 76))
print(multiply(5, 12))

class Person:
	def __init__(self, name, id):
		self._id = id
		self._name = name

	def get_name(self):
		return self._name

	def get_age(self):
		return self.age

sree = Person('sreekanth', 1918)

sree.__dict__['age'] = 27

print(sree.get_name())
print(sree.get_age())