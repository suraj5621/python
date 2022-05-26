#hamming distance======> 
def h(a,b):
	c=a^b
	d=bin(c)
	e=d.count('1')
	print(e)
x=int(input())
y=int(input())
h(x,y)