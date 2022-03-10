a=int(input('enter the first side'))
b=int(input('enter the second side'))
c=int(input('enter the third side'))
if a+b>c or b+c>a or c+a>b:
	if a==b==c:
		print("equatorial triangle")
	elif a==b!=c or b==c!=a or c==a!=b:
		print("isosceles triangle")
	else:
		print("scalene triangle")		
