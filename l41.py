# armstrong no.



n=int(input('enter the no.'))
b=n
l=n
s=0
i=0

while b:
	b=b//10
	i=i+1
while n:
	rem=n%10
	s=s+rem**i
	n=n//10
	
if s==l:
	print("armstrong")
else:
	print("not")			
	
