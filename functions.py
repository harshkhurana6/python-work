def cube(n):
  c=n**3
  print("cube of",n,"is",c)

num=int(input("enter any no:"))
cube(num)

def sum(x,y):
  z=x+y
  return z
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=sum(a,b)
print("sum of",a,"and",b,"is",c)
c=sum(y=a,x=b)

def square(n):
  c=n**2
  print("square of",n,"is",c)

y=int(input("Enter any no:"))
square(y)

def swap(x,y):
  return y,x
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
a,b=swap(a,b)
print(a,b)

def swap(x,y):
  temp=x
  x=y
  y=temp
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print(a,b)
swap(a,b)
print(a,b)


def swap(l2):
  nl=[1,2]
  l2=nl
  temp=l2[0]
  l2[0]=l2[1]
  l2[1]=temp
l1=[10,20]
print(l1)
swap(l1)
print(l1)

def sum(x,y=5):
  z=x+y
  return z

a=int(input("Enter any number:"))
b=int(input("Enter any number:"))
c=sum(a,b)
print(c)
c=sum(a)
print(c)
c=sum(b)
print(c)





def sum(x,y):
  return x+y
  

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=sum(a,b)
print("sum of",a,"and",b,"is",c)

x=2
y=3
z=sum(x,y)
print("sum of",x,"and",y,"is",z)


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

def getsum(n):
  sum=0
  while(n!=0):
    
    sum=sum+int(n%10)
    n=int(n/10)
  return sum

n=687
print(getsum(n))
