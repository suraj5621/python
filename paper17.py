d={'ram':55, 'madhav':87, 'ajay':98, 'slit':89}

# find the maximum value 

c=max(d.values())
print(c)

for i in d:
	if d[i]==c:	
		print(i)