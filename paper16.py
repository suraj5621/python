					create dict  {1:0, 2:1, 3:1, 4:2, 5:3, .......}  fibnacii dictonary

d={}
n=int(input())
i=1
a=0
b=1
while i<=n:
	if i==1:
		d[i]=a
	elif i==2:
		d[i]=b
	elif i>2:
		c=a+b
		d[i]=c
		a=b
		b=c
	i=i+1
print(d)