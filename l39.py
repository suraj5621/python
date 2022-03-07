# to find the reverse of a no.



n=int(input('enter the no.'))
s=0
while n:
	rem=n%10
	s=s*10+rem
	n=n//10
	
print('reverse of the digit is ',s)	
