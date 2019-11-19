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

a=np.array([1,2,3],float)
b=np.array([5,2,6],float)
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(a%b)
print(b**a)

a=np.array([[1,2],[3,4]],float)
b=np.array([[2,0],[1,3]],float)
print(a*b)

value error
a=a=np.array([1,2,3],float)
b=np.array([4,5],float)
print(a+b)


a=np.array([[1,2],[3,4],[5,6]],float)
b=np.array([-1,3],float)
print(a)
print(b)
print(a+b)

a=np.zeros((2,2),float)
b=np.array([-1,3],float)
print(a)
print(b)
print(a+b)
print(a+b[np.newaxis,:])
print(a+b[:,np.newaxis])


a=np.array([1,4,9],float)
print(np.sqrt(a))

a=np.array([1.1,1.5,1.9],float)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

print(np.pi)

print(np.e)


a=np.array([1,4,5],int)
for x in a:
    print(x)

a=np.array([[1,2],[3,4],[5,6]],float)
for x in a:
    print(x)

a=np.array([[1,2],[3,4],[5,6]],float)
for (x,y) in a:
    print(x*y)

a=np.array([2,4,3],float)
print(a.sum())
print(a.prod())
print(np.sum(a))
print(np.prod(a))

a=np.array([2,1,9],float)
print(a.mean())
print(a.var())
print(a.std())

a=np.array([2,1,9],float)
print(a.min())
print(a.max())
print(a.argmin())
print(a.argmax())


a=np.array([6,2,5,-1,0],float)
print(sorted(a))
print(a.sort())
print(a.clip(0,5))

a=np.array([1,1,4,5,5,5,7],float)
print(np.unique(a))

a=np.array([[1,2],[3,4]],float)
print(a.diagonal())

a=np.array([1,3,0],float)
b=np.array([0,3,2],float)
print(a>b)
print(a==b)
print(a<=b)


a=np.array([1,3,0],float)
print(a>2)

c=np.array([True,False,False],bool)
print(any(c))
print(all(c))

a=np.array([1,3,0],float)
print(np.logical_and(a>0,a<3))

b=np.array([True,False,False],dtype=bool)
print(np.logical_not(b))

c=np.array([False,True,False],dtype=bool)
print(np.logical_or(b,c))

a=np.array([1,3,0],float)
print(np.where(a!=0,1/a,a))
print(np.where(a>0,3,2))

a=np.array([[0,1],[3,0]],float)
print(a.nonzero())

a=np.array([1,np.NaN,np.Inf],float)
print(a)
print(np.isnan(a))
print(np.isfinite(a))


a=np.array([[6,4], [5,9]],float)
print(a>=6)
print(a[a>=6])
sel=(a>=6)
print(a[sel])
print(a[np.logical_and(a>5,a<9)])


a=np.array([2,4,6,8],float)
b=np.array([0,0,1,3,2,1],int)
print(a[b])
print(a[[0,0,1,3,2,1]])
print(a.take(b))

a=np.array([[1,4],[9,16]],float)
b=np.array([0,0,1,1,0],int)
c=np.array([0,1,1,1,1],int)
print(a[b,c])

a=np.array([[0,1],[2,3]],float)
b=np.array([0,0,1],int)
print(a.take(b,axis=0))
print(a.take(b,axis=1))


a=np.array([0,1,2,3,4,5],float)
b=np.array([9,8,7],float)
a.put([0,3],b)
print(a)

a=np.array([0,1,2,3,4,5],float)
a.put([0,3],5)
print(a)

a=np.array([1,2,3],float)
b=np.array([0,1,1],float)
print(np.dot(a,b))

a=np.array([[0,1],[2,3]],float)
b=np.array([2,3],float)
c=np.array([[1,1],[4,0]],float)
print(np.dot(b,a))
print(np.dot(a,b))
print(np.dot(a,c))


