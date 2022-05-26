				# frequency of dict.values

d={}
n=int(input())
l=[ ]
for i in range(1,n+1):
	d[i]=input()
	l.append(d[i])
z=''.join(l)
a=set(z)
for j in a:
	print(j,z.count(j))

