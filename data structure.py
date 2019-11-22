traversal
a=[10,20,30,40,50]
i=0
while i<=len(a)-1:
    print(a[i])
    i=i+1


2nd method Traversal
    
a=[10,20,30,40,50]
for i in range(len(a)):
    print(a[i])



inserting

a=[10,20,30,40,50]
a.insert(3,750)
print(a)


deleting
a=[10,20,30,40,50]
a.pop(3)
print(a)





 bubble sort

a=[5,4,3,2,1]
temp=0
n=len(a)
for i in range(1,n):
  for j in range(n-i):
    temp=a[j]
    a[j]=a[j+1]
    a[j+1]=temp
print(a)


linear search

import sys
a=[10,20,30,40,50]
item=int(input("Enter the number for search:"))
i=0
n=len(a)
for i in range(n):
  if a[i]==item:
    print(i)
    print("search successful")
    sys.exit(0)

print("search not successfull")



binary search

import sys
a=[10,20,30,40,50]
item=int(input("Enter the number for search:"))
l=0
h=len(a)-1
while l<=h:
  m=(l+h)//2
  if item==a[m]:
    print(m)
    sys.exit(0)
  elif item>a[m]:
    l=m+1
  else:
    h=m-1

print("item does not exist")




selection sort
a=[50,40,30,20,10]
temp=0
n=len(a)
minn=0
for i in range(0,n-1):
  minn=a[i]
  for j in range(i+1,n):
    if a[j]<minn:
      temp=a[j]
      a[j]=minn
      minn=temp
  a[i]=minn

print(a)


insertion sort

a=[6,4,1,3,2]
n=len(a)
temp=0
p=0
for k in range(1,n):
    temp=a[k]
    p=k-1
    while a[p]>temp and p>=0:
        a[p+1]=a[p]
        p=p-1
    a[p+1]=temp
    
print(a)


merging

a=[2,5,10,12]
b=[1,3,15,20]
c=[]
i=0
j=0
l1=len(a)
l2=len(b)
while i<l1 and j<l2:
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
if i==l1:
    for p in range(j,l2):
        c.append(b[p])
else:
    for p in range(i,l1):
        c.append(a[p])

print(c)
        


2D arrays

addition of arrays
a=[[2,4],[6,10]]
b=[[8,10],[12,14]]
c=[]
m=len(a)
n=len(b)
for i in range(0,m):
    for j in range(0,n):
        c.append(a[i][j]+b[i][j])
print(c)


transpose of array


m=2
n=3

def transpose(a,b):
    for i in range(0,n):
        for j in range(0,m):
            b[i][j]=a[j][i]
a=[[10,20,30],[40,50,60]]
b=[[0 for x in range(m)] for y in range(n)]  
transpose(a,b)

print("Result matrix is") 
for i in range(n): 
    for j in range(m): 
        print(b[i][j], " ", end='') 
    print()


stack pop

stack=[]
stack.append('a') 
stack.append('b') 
stack.append('c')
print("initial stack")
print(stack)

print("Elements poped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("stack after elements are poped:")
print(stack)


stack push

stack=[]

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)
