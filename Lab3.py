#Задание 1

a = [1,0,3,4,0,6,7,8,9,0]

def adder(a):
	p = sum(a)
	a = print(p)
	return a
	
	
adder(a)

#задание 2

def countit(B):
	x= B.count(0)
	x = print(x)
	return x
	
print()
countit(a)
print()

#задание 3

def triangular(n):
	for i in range(n):
		for j in range(i+1):
			print(j+1, end=' ')
		print()
			
triangular(4)
			
#задание 4

def pyramid(q):
	
	for i in range(1, q + 1):
		for j in range(1,q + 1-i):
			print(' ', end = ' ')
			
		for j in range (1,i + 1):
			print(j, end=' ')
			
		for j in range(i -1, 0, -1):
				print(j, end= ' ')
		print()
				
pyramid(5)
				
				

