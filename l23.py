# triangle valid or not
a=int(input('enter the first side'))
b=int(input('enter the second side'))
c=int(input('enter the third side'))
if a+b>c or b+c>a or c+a>b:
	print('triangle is valid')
else:
	print('triangle is not valid')	
