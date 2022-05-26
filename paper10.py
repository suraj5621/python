#sort dictonary on the basis of values
d1={}
d2={}
l=[]
n=int(input())
for i in range(n):
	key=input()
	value=input()
	d1[key]=value
	l.append(value)
l.sort()
for j in l:
	for k in d1:
		if j==d1[k]:
			d2[k]=j
print(d2)		
