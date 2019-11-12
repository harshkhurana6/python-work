s=set()
s={1,2,3}
print(type(s))

str="hello"
s=set(str)
print(s)


t=(1,20,30)
s=set(t)
print(s)

l=[1,1,3,4,3,5,2,2,5,5]
s=set(l)
print(s)
l1=list(s)
l1.sort()
for i in s:
  print(i)
s.add(6)
print(s)
s.add((7,8))
print(s)
s.clear()
print(s)


s1={1,2,3}
s2=s1
print(id(s1),id(s2))
print(s1,s2)
s2.clear()
print(s1,s2)


s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
s3=s1|s2
print(s3)
print(s1-s2)
print(s1-s2-s3)
print(s1-s2-s3)
s1=s1-s2
print(s1,s2)

s1={1,2,3}
s2={2,3,4}
s3=s1^s2
print(s3)

s1={1,2,3}
s2={2,3,4}
s3=s1&s2
print(s3)


s={"a","b","c","d"}
s1=s
s1.discard("b")
print(s1)
s1.discard("z")
print(s1)
s1.remove("z")
print(s1)

s={"a","b","c","d"}
s1=s
print(s1.pop())
s1.pop()
print(s1)


s1={1,2,3,4,5}
s2={2,3}
print(s2.issubset(s1))
print(s2.issuperset(s1))

import functools

l=[1,2,3,4]
sum=functools.reduce(lambda x,y:x+y,l)
print(sum)

n=int(input("enter any no:"))
sum=functools.reduce(lambda x,y:x+y,range(1,n+1))
print(sum)

l=[5,4,9,2,7,10]
f=lambda a,b: a if (a>b) else b
print(functools.reduce(f,l))


l=[5,4,6,8,10,12,16,7,9,11,51,2]
result=filter(lambda x:x%2==0,l)
print(list(result))
