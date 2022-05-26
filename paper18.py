			# wap to input the value of n and then take radius of circle then create a dict. in which radius acting as key and its circumfrences acting like value

d={}
n=int(input())
for i in range(n):
	key=int(input('entyer the radius'))
	
	d[key]=2*3.14*key
print(d)