import inspect

class Hack():
	def ha(self):
		pass

	def goof(self):
		pass

	def GoT(self):
		pass

	def kill(self):
		pass

b = inspect.getmembers(Hack)
# print(b)

mem = [(k,v) for k, v in b if k[0] != '_']
for i in mem:
	print(i[0])

def hack(a,b,c):
	return a+b+c

def hack(a,b):
	return a*b
# It will conider the last function
if __name__ == '__main__':
	print(hack(2,3))
	print(hack(4,5))
