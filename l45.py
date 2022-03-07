# strong no.



n=int(input('enter the no'))
b=n
r=1
s=0
while n:
	rem=n%10
	r=1
	i=1
	while i<=rem:
		r=r*i
		i=i+1
	s=s+r	
	n=n//10
if s==b:
	print("strong no.")
else:
	print("not strong")		
