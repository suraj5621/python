# to find the area of scalen triangle
a=int(input('enter the first side'))
b=int(input('enter the second side'))
c=int(input('enter the third side'))
if a!=b!=c:
	s=(a+b+c)/2
	area=(s*(s-a)*(s-b)*(s-c))**0.5
	print('area is',area)
else:
	print('it is not scalen triangle')	
