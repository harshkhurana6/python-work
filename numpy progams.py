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


a=np.array(range(10),float)
##print(a)
a=a.reshape((5,2))
print(a)
print(a.shape)

a=np.array([1,2,3],float)
b=a
c=a.copy()
a[0]=0
print(a)
print(b)
print(c)

a=np.array([1,2,3],float)
print(a.tolist())
s=a.tostring()
print(s)
print(np.fromstring(s))

a=np.array([1,2,3],float)
print(a)
print(a.fill(0))

a=np.array(range(6),float).reshape((2,3))
print(a)

a=np.array([[1,2,3],[4,5,6]],float)
print(a)
print(a.flatten())

a=np.array([1,2],float)
b=np.array([3,4,5,6],float)
c=np.array([7,8,9],float)
print(np.concatenate((a,b,c)))

a=np.array([[1,2],[3,4]],float)
b=np.array([[5,6],[7,8]],float)
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

a=np.array([1,2,3],float)
print(a)
print(a[:,np.newaxis])
print(a[:,np.newaxis].shape)
print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)


print(np.arange(5,dtype=float))
print(np.arange(1,6,2,dtype=int))

print(np.ones((2,3),dtype=float))

print(np.zeros(7,dtype=int))


print(np.identity(4, dtype=float))

print(np.eye(4, k=1, dtype=float))
