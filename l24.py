# find profit percentage and loss percentage
cp=float(input('enter the cost price '))
sp=float(input('enter the selling price '))
a=sp-cp
if a>0:
	b=(a/cp)*100
	print('profit is',b,'%')
else:
	b=(a/cp)*100	
	print('loss is',abs(b),'%')
