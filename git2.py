def ha():
	print("Hacker Online")

class Hacker():
	def __init__(self, name, age):
		self._name = name
		self._age = age

	def get_name(self):
		return self._name

	def get_age(self):
		return self._age

	def get_marks(self):
		return self.marks

	@classmethod
	def set_mark(cls, marks):
		cls.marks = marks

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

std1 = Hacker('Sree', 25)

Hacker.set_mark(56)

print(std1.get_marks())

print(std1.get_name())

import datetime

my_date = datetime.date(2016, 9, 12)

print(Hacker.is_workday(my_date))