# print pattern with double while loop
n=int(input('enter the no. of rows'))
i=1
j=1
while i<=n:
	while j<=i:
		print('*'*j,end='')
		j=j+1
	i=i+1
	print('')
