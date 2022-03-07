# take one no. from the user and find the sum of digits



n=int(input('enter the no.'))
s=0
while n:
	rem=n%10
	s=s+rem
	n=n//10
print('sum of the digit is ',s)	
