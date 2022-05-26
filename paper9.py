import numpy as np
a= np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
b= np.array([[13,14,15], [16,17,18],[2,4,6]])
print(np.concatenate((a,b),axis=0))
print()
print(np.concatenate((a,b),axis=1))