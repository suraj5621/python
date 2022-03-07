# print all armstrong no. 1 to n


n=int(input('enter value'))

j=1
while j<=n:
	s=0
	b=j
	l=j
	i=0
	c=j
	while b:
		b=b//10
		i=i+1
	while c:
		rem=c%10
		s=s+rem**i
		c=c//10
	
	if s==l:
		print(s)
	j=j+1
