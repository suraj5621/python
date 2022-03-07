# input three no. find the greatest no.
a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
	print('greatest is ',a)
elif b>a and b>c:
	print('greatest is ',b)
else:
	print('greatest is ',c)
