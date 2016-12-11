class Mammals:
	def __init__(self):
		'''Constructor for this class'''
		# Create some member animals
		self.members = ['Tiger', 'Elephant', 'Wild Cat']

	def printMembers(self):
		print('Printing members of the Mammals class')
		for mem in self.members:
			print(mem)
