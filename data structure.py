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

2nd method to use push pop peek  in stack

class stacknode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack:
    def __init__(self):
        self.root=None
    def isempty(self):
        return True if self.root is None else False
    def push(self,data):
        newnode=stacknode(data)
        newnode.next=self.root
        self.root=newnode
        print("%d pushed to stack"%(data))
    def pop(self):
        if(self.isempty()):
            return float("-inf")
        temp=self.root
        self.root=self.root.next
        popped=temp.data
        return popped 
      
    def peek(self): 
        if self.isempty(): 
            return float("-inf") 
        return self.root.data
stack = stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
print ("%d popped from stack"%(stack.pop()))
print ("Top element is % d " %(stack.peek()))




factorial of a number

def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return fact


x=factorial(3)
print(x)
x=factorial(2)
print(x)
n=int(input("Enter any no."))
x=factorial(n)
print(x)



fibonacci series


def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))


Queue using list

queue=[]
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial Queue")
print(queue)

print("\nElements poped from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))


print("\nQueue after elemets poped from it")
print(queue)


Queue using collections.dequeue

from collections import deque
q=deque()
q.append('a')
q.append('b')
q.append('c')

print("Intial Queue")
print(q)

print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)


Python program for array implementation of queue

class queue:
    def __init__(self,capacity):
        self.front=self.size=0
        self.rear=capacity-1
        self.q=[None]*capacity
        self.capacity=capacity

    def isfull(self):
        return self.size==self.capacity
    def isempty(self):
        return self.size==0
    def enqueue(self,item):
        if self.isfull():
            print("full")
            return
        self.rear=(self.rear+1)%self.capacity
        self.q[self.rear]=item
        self.size=self.size+1
        print("%s enqueued to queue" %str(item))
    def dequeue(self):
        if self.isempty():
            print("Empty")
            return
        print("%s dequeued from queue" %str(self.q[self.front]))
        self.front=(self.front+1)%(self.capacity)
        self.size=self.size-1

    def que_rear(self):
        if self.isempty():
            print("queue is empty")
        print("Rear item is",self.q[self.rear])

    def que_front(self):
        if self.isempty():
            print("queue is empty")
        print("front item is",self.q[self.front])

if __name__=='__main__':
    Queue=queue(30)
    Queue.enqueue(10)
    Queue.enqueue(20)
    Queue.enqueue(30)
    Queue.enqueue(40)
    Queue.dequeue()
    Queue.que_rear()
    Queue.que_front()
    


Deque with python

import collections

de=collections.deque([1,2,3])
de.append(4)
print("The deque after appending at right is:")
print(de)
de.appendleft(6)
print("The deque after appending at left is:")
print(de)
de.pop()
print("The deque after deleting element from right is:")
print(de)
de.popleft()
print("The deque after deleting element from left is:")
print(de)


from collections import deque

de=deque([1,4,3,3,4,2,4])
print(de)
print("The number 4 first occurs at a position=:")
print(de.index(4,2,5))
de.insert(4,3)
print("The deque after inserting 3 at 5th position:")
print(de)
print("The count of 3 in deque is:")
print(de)
de.remove(3)
print("The deque after deleting first occurrence of 3 is:")
print(de)

from collections import deque
de=deque([1,2,3])
print("The deque after exting at the end ia:")
de.extend([4,5,6])
print(de)
de.extendleft([7,8,9])
print("The deque after extending at begining is:")
print(de)
de.rotate(-3)
print("The deque after rotating first three elements to the back of it is:")
print(de)
de.reverse()
print("The deque after revesing is:")
print(de)



