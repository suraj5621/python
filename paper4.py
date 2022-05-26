import numpy as np
a=list(map(int,input().split()))
c=np.array(a)
print(type(c))
print(c[::-1])
print(np.flipud(c))