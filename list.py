l=[10,20,'ram',(2,3),{"name:":"mohan"}]
print(l[4])

l=[1,2,3,4,5]
print(l[0])
print(l[2:4])
print(l[-2:])
print(l[::-1])

l=[1,2,3,4,5]
print(l)
l[1]=200
print(l)
del(l[1])
print(l)

print([1,2,3]+[4,5,6])

l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

print([1,2]*2)

print(10 in [1,2,3])

print('p' in 'python')

for item in [10,20,30]:
  print(item)

l=[1,2,3]
for item in l:
  print(item)
for i in range (len(l)):
  print(l[i])
for index,item in enumerate(l):
  print("item at",index,'index is',item)

print(list(enumerate(l)))

l=[1,2,3,4,5]
x=len(l)
l=list(range(1,6))
print(len(l))

l=[10,20,30]
print(max(l))
print(min(l))
print(sum(l))

t=(1,2,3)
l=list(t)
print(l)
l[2]=300
print(l)
t=tuple(l)
print(t)

s='hello'
l=list(s)
print(l)
str=" ".join(l)
print(str)

l1=['c','c++','jawa']
l1.append('python')
print(l1)

l1=[1,2,3]
l2=[4,5]
l1.extend(l2)
print(l1)

l=[10,20,30,10,40]
print(l.count(10))

l=['red','blue','green']
print(l.index('blue'))
print(l.index('orange'))

l=['apple','mango','banana']
l.insert(1,'orange')
print(l)

l=['apple','mango','banana']
l.insert(1,[3,4,5])
print(l)

l=[10,20,30,40]
l.pop()
print(l)
l.pop(1)
print(l)

l=['red','blue','green']
l.remove('blue')
print(l)

l=[10,20,30]
l.reverse()
print(l)

l=[10,20,30,50,120,570,15,25,76,42]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l=[10,40,30,50,20]
print(l)
l1=sorted(l)
print(l1)
l1=sorted(l,reverse=True)
print(l1)

l=[(1,3),(4,2),(2,6)]
l.sort()
print(l)
