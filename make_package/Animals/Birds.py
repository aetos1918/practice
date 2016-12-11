class Birds:
	def __init__(self):
		'''Constructor for this class'''
		# Create some member animals
		self.members = ['Sparrow', 'Robin', 'Duck']

	def printMembers(self):
		print('Printing members of the Mammals class')
		for mem in self.members:
			print(mem)
