#WAP to find the second maximum no. in an list
import numpy as np
l1 =list(map(int, input().split()))
l=max(l1)
a=l1.count(l)
for i in range(a):
    l1.remove(l)
v=max(l1)
print(v)    