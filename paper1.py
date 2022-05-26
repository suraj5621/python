#WAP to find the frequency of a string
a='my name is suraj'
f={}
for i in a:
	f[i]=f.get(i,0)+1
for j in f:
	print(j,f[j])