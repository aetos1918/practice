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

# Fibonaci Series
def fibo(ab):
	a, b =1,1
	for i in range(ab):
		print(a, end=" ")
		a,b = b,a+b


def fib_gen(ab):
	a,b = 1,1
	for i in range(ab):
		yield a
		a,b = b, a+b

print(list(fib_gen(6)))

# Factorial
def facto(ab):
	op = reduce(lambda a,b: a*b, range(1, ab+1))
	print(op)


# String reverse Check
def check_poly(strv):
	# Remove all white spaces from a string
	cln = strv.replace(" ","")
	# Reversing a String
	cln_r = cln[::-1]
	if cln == cln_r:
		print("Given String '{}' is a polyndrome".format(strv))
	else:
		print("Given String '{}' is not a polyndrome".format(strv))

#check_poly("Hacker Online") # Not poly
str = "abcdeffedcba" # Poly

# Triangle of numbers
#print("\t"*2+'Triangle of Numbers')

def tri_pat(no_rows):
	for i in range(1, no_rows):
		for j in range(i):
			print(1, end=" ")
		print('\n')


# Pyramid Structure
def pyramid(no_rows):
	for i in range(1, no_rows+1):
		for j in range( no_rows-i, -1, -1):
			if j > 0:
				print(' ', end='')
		for k in range(i):
			print('*', end=' ')
		print('\n')
	for i in range(no_rows-1, -1, -1):
	    for j in range(no_rows-i):
		    print(' ', end='')
	    for k in range(i):
		    print('*', end=' ')
	    print('\n')

# Pyramid (odd)

def pyramid_odd(no_rows):
	for i in range(1, no_rows):
		for j in range(no_rows-i):
			print(' ', end='')
		for j in range(1, i):
			print(j, end='')
		for j in range(1,i):
			print(j, end='')
		print('\n')

# unstructure list to single list
op = []
def uni_lst(lst):
    if type(lst) in [list, tuple]:
        for x in lst:
            if type(x) in [list, tuple]:
                uni_lst(x)
            else:
                op.append(x)
    return op
ab = [1,2,3,[4,5,6,(7,8,9)],(10,11,12),[13,14]]

if __name__ == '__main__':
	fibo(5)
	fib_gen(5)
	facto(5)
	check_poly(str)
	tri_pat(5)
	pyramid(5)
	pyramid_odd(5)
	print(uni_lst(ab))
