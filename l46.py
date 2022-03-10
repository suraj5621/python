# input mobile no 10 digit and check even places or odd places sum is equal then we can say its a magic no.
n= int(input('enter the mobile no.'))
s=0
r=0
i=0
while n:
	rem=n%10
	i=i+1
	if i%2==0:
		s=s+rem
	elif i%2!=0:
		r=r+rem
	n=n//10
if(s==r):
	print("magic no.")	
else:
	print("not magic no.")			

