# prime no. in range


n=int(input('enter the no.'))
j=1
print("all prime no. with in range of 1 to %d"%n)
while j<=n:
	i=1
	c=0
	while i<=j:
		if j%i==0:
			c=c+1
		i=i+1
	if c==2:
		print(j)	
	j=j+1		
