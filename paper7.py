import numpy as np
k=list(map(int,input().split()))
l=list(map(int,input().split()))
r=int(input('rows enter'))
c=int(input('column enter'))
x=np.array(k)
z=np.array(l)
a=x.reshape(r,c)
b=z.reshape(r,c)
add=np.add(a,b)
sub=np.subtract(a,b)
mul=np.multiply(a,b)
div=np.divide(a,b)
floor=np.floor_divide(a,b)
mod=np.mod(a,b)
power=np.power(a,b)
print(add)
print(sub)
print(mul)
print(div)
print(floor)
print(mod)
print(power)
print(a)
print(b)