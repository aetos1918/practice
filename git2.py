def ha():
	print("Hacker Online")

class Hacker(obect):
	def __init__(self, name, age):
		self._name = name
		self._age = age

	@staticmethod
	def get_name():
		return Hacker._name

	@classmethod
	def get_age(cls):
		return cls._age