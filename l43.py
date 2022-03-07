# no. is prime no. or not


n=int(input('enter value'))
i=1
c=0
while i<=n:
	if n%i==0:
		c=c+1
	i=i+1		
if c==2:
	print("prime no.")
else:
	print("not prime")
	i=i+1			
