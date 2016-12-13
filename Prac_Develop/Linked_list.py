# Linked List
class Node:
	def __init__(self, d, n=None):
		self.data = d
		self.next_node = n

	def get_next(self):
		return self.next_node
	def set_next(self, n):
		self.next_node = n
	def get_data(self):
		return self.data
	def set_data(self, d):
		self.data = d

class LinkedList:
	def __init__(self, r=None):
		self.root = r
		self.size = 0
	def get_size(self):
		return self.size
	def add(self, d):
		new_node = Node(d, self.root)
		self.root = new_node
		self.size += 1
	def remove(self, d):
		this_node = self.root
		prev_node = None
		while this_node:
			if this_node.get_data() == d:
				if prev_node:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node
				self.size -= 1
				return True
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False
	def find(self, d):
		this_node = self.root
		while this_node:
			if this_node.get_data() == d:
				return d
			else:
				this_node = this_node.get_next()
		return None

# myList = LinkedList()
# myList.add(5)
# myList.add(8)
# myList.add(12)

# print(myList.size)

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda student: student.age))   # sort by age

from operator import itemgetter, attrgetter, methodcaller

# sorted(student_tuples, key=itemgetter(2))

sorted(student_objects, key=attrgetter('age'))

# sorted(student_tuples, key=itemgetter(1,2))