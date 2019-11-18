import numpy as np
a = np.array([1, 4, 5, 8], float)
print(a)

a = np.array([1, 4, 5, 8], float)
print(a[:2])

a = np.array([1, 4, 5, 8], float)
print(a[3])

a = np.array([1, 4, 5, 8], float)
a[0]=5
print(a)


a=np.array([[1,2,3],[4,5,6]],float)
print(a)
print(a[0,0])
print(a[0,1])
print(a[1,2])
print(a[1,1])

a=np.array([[1,2,3],[4,5,6]],float)
print(a[1,:])
print(a[:,2])
print(a[-1:,-2:])
print(a[-1:,-3:])
print(a[-2,-1:])
print(a.shape)
print(a.dtype)
print(len(a))
print(2 in a)
print(0 in a)
