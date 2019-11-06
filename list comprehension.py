l=[i**2 for i in range(1,11)]
print(l)

l=[i for i in range(1,6)]
print(l)

l=[x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']]
print(l)

l=[[1,2,3],[4,5,6],[7,8,9]]
l=[ele for row in l for ele in row]
print(l)

l=[x for x in "I AM YOUR COMPANION" if x not in ['A','E','I','O','U']]
print(l)

t1=('name','age','phone')
t2=('Ram',20,9896000000)
d={}
for i in range(len(t1)):
  d[t1[i]]=t2[i]
  print(d)
d={t1[i]:t2[i] for i in range (len(t1))}
print(d)

l1=[1,2,3]
l2=[4,5,6]
l=[i for i in l1 for j in l2 if i==j]
print(l)

l=[1,2,3]
l1=[[i**2,i**3] for i in l]
print(l1)

l=['H','E','L','L','O']
l1=[i.lower() for i in l]
print(l1)

l2=list("".join(l).lower())
print(l2)
