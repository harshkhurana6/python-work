class rectangle:
  def __init__(self):
    self.l=2
    self.b=4
  def getdata(self):
    self.l=int(input("Enter the l:"))
    self.b=int(input("Enter the b:"))
  def area(self):
    print("Area is:",(self.l*self.b))

r1=rectangle()
r2=rectangle()
r1.area()
r2.area()
r1.getdata()
r2.getdata()
r1.area()
r2.area()

class room:
  def __init__(self):
    self.l=2
    self.b=4
    self.h=6
  def getdata(self):
    self.l=int(input("Enter the l:"))
    self.b=int(input("Enter the b:"))
    self.h=int(input("Enter the h:"))
  def volume(self):
    print("Volume is:",(self.l*self.b*self.h))
  def TSA(self):
    print("Total Surface Area is:",(2*((self.l*self.b)+(self.b*self.h)+(self.h*self.l))))

ro1=room()
ro2=room()
ro1.volume()
ro2.volume()
ro1.TSA()
ro2.TSA()
ro1.getdata()
ro2.getdata()
ro1.volume()
ro2.volume()
ro1.TSA()
ro2.TSA()

class interest:
  def __init__(self):
    self.p=10000
    self.r=20
    self.t=1
  def getdata(self):
    self.p=int(input("Enter the p:"))
    self.r=int(input("Enter the r:"))
    self.t=int(input("Enter the t:"))
  def SI(self):
    print("Simple Interest is:",((self.p*self.r*self.t)//100))
  def CI(self):
    print("Compound Interest is:",(self.p*((1+(self.r/100))**self.t)-self.p))

i1=interest()
i2=interest()
i1.SI()
i2.CI()
i1.getdata()
i2.getdata()
i1.SI()
i2.CI()


class rectangle:
  def __init__(self,x,y):
    self.l=x
    self.b=y
  def getdata(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return self.l*self.b
r1=rectangle(2,4)
print("Area is:",r1.area())
r1.getdata(3,5)
print("Area is:",r1.area())
p=int(input("Enter l:"))
q=int(input("Enter b:"))
r2=rectangle(p,q)
ar=r2.area()
print("Area is:",ar)
p=int(input("Enter l:"))
q=int(input("Enter b:"))
r2.getdata(p,q)
ar=r2.area()
print(ar)


class room:
  def __init__(self,x,y,z):
    self.l=x
    self.b=y
    self.h=z
  def getdata(self,l,b,h):
    self.l=l
    self.b=b
    self.h=h
  def volume(self):
    return self.l*self.b*self.h
v1=room(6,5,7)
print("Volume is:",v1.volume())
p=int(input("Enter l:"))
q=int(input("Enter b:"))
r=int(input("Enter h:"))
v2=room(p,q,r)
vr=v2.volume()
print("Volume is:",vr)
p=int(input("Enter l:"))
q=int(input("Enter b:"))
r=int(input("Enter h:"))
v2.getdata(p,q,r)
vr=v2.volume()
print(vr)


class bank:
  def __init__(self,a,b,n):
    self.an=a
    self.ba=b
    self.na=n
    
  def getdata(self,accno,bal,nam):
    self.an=accno
    self.ba=bal
    self.na=nam
    
  def deposit(self,amt):
    self.ba=self.ba+amt
    
  def withdraw(self,amt):
    self.ba=self.ba-amt

    
  def display(self):
    print("Account number:",self.an,"balance is:",self.ba,"Account Name:",self.na)
    
b1=bank(123456,5000,"Harsh Khurana")
b1.deposit(2000)
b1.display()
b1.withdraw(1000)
b1.display()
p=int(input("Enter the account number:"))
q=int(input("Enter the balance amount:"))
r=input("Name of the account:")
b2=bank(p,q,r)
y=int(input("Enter the amount to deposite:"))
b2.deposit(y)
b2.display()
s=int(input("Enter the amount to withdraw:"))
b2.withdraw(s)
b2.display()
b2.getdata(p,q,r)
k=int(input("Enter the amount to deposite:"))
b2.deposit(k)
b2.display()
l=int(input("Enter the amount to withdraw:"))
b2.withdraw(l)
b2.display()


class employee:
  def __init__(self,f,l,s):
    self.fn=f
    self.ln=l
    self.sal=s
  def getdata(self,a,b,c):
    self.fn=a
    self.ln=b
    self.sal=c
    
  def fullname(self):
    print(self.fn+self.ln)
    return(self.fn+self.ln)
    
    
  def email(self):
    print(self.fullname()+"@company.com")
    
  def display(self):
    print("First Name:",self.fn,"Last name:",self.ln,"Salary:",self.sal)

e1=employee("Harsh","Vardhan",800000)

e1.fullname()
e1.display()
e1.email()
e1.display()
p=input("First name:")
q=input("Last name:")
r=int(input("salary:"))
e2=employee(p,q,r)
e2.fullname()
e2.display()
e2.email()
e2.display()
p=input("First name:")
q=input("Last name:")
r=int(input("salary:"))
e2.getdata(p,q,r)
e2.fullname()
e2.display()
e2.email()
e2.display()



class circle:
  def __init__(self,r):
    self.ra=r
  def getdata(self,rad):
    self.ra=rad
  def area(self):
    return(2*3.14*self.ra*self.ra)
  def circumference(self):
    return(2*3.14*self.ra)

c1=circle(20)
ar=c1.area()
cr=c1.circumference()
print("Area is:",ar)
print("Circumference is:",cr)
radius=int(input("Enter the radius:"))
c2=circle(radius)
AR=c2.area()
CR=c2.circumference()
print("Area is:",AR)
print("Circumference is:",CR)
Radius=int(input("Enter the radius:"))
c2.getdata(Radius)
print("Area is:",AR)
print("Circumference is:",CR)

class rectangle:
  def getdata(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return self.l*self.b
rectlist=[]
z=[]
for i in range(3):
  r=rectangle()
  x=int(input("Enter l:"))
  y=int(input("Enter b:"))
  r.getdata(x,y)
  rectlist.append(r)
for i in range(3):
  z.append(rectlist[i].area())
print(z)


class number:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def display(self):
    print("x is:",self.x,"y is:",self.y)
  def sum(self,p):
    temp=number(0,0)
    temp.x=self.x+p.x
    temp.y=self.y+p.y
    return temp
a=number(10,20)
b=number(2,4)
c=a.sum(b)
c.display()

class employee:
  def __init__(self,ecode,ename,salary):
    self.ecode=ecode
    self.ename=ename
    self.salary=salary
  def putdata(self):
    print(self.ecode,self.ename,self.salary)
class salesman(employee):
  def __init__(self,ecode,ename,salary,commision):
    super().__init__(ecode,ename,salary)
    self.commision=commision
  def putcommsion(self):
    self.putdata()
    print("Commsion is:",self.commision)
    print("Total salary:",(self.salary+self.commision))

s=salesman(1001,"abc",20000,5000)
s.putcommsion()


class time:
  def __init__(self,hrs,mins):
    self.hrs=hrs
    self.mins=mins
  def display(self):
    print("hrs is:",self.hrs,"mins is:",self.mins)
  def sum(self,p):
    temp=time(0,0)
    temp.hrs=self.hrs+p.hrs
    temp.mins=self.mins+p.mins
    if (temp.mins>=60):
      temp.mins=temp.mins-60
      temp.hrs=temp.hrs+1
    return temp
t1=time(2,30)
t2=time(4,50)
t3=t1.sum(t2)
t3.display()

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
      print("Name is:",self.name)
      print("Age is:",self.age)
  def greater(self,p):
    if (p.age>self.age):
      return p
    else:
      return self
      
a=person("Abc",90)
b=person("PQR",80)
c=a.greater(b)
c.display()





class rectangle:
  def getdata(self,l,b):
    self.l=l
    self.b=b
  def area(self):
    return(self.l*self.b)
  def greater(self,p):
    if (self.area()>p.area()):
      return self
    else:
      return p
  def display(self):
    print("Length is:",self.l)
    print("Breadth is:",self.b)
    print("Area is:",self.area())


r1=rectangle()
x=int(input("Enter l:"))
y=int(input("Enter b:"))
r1.getdata(x,y)
r2=rectangle()
x=int(input("Enter l:"))
y=int(input("Enter b:"))
r2.getdata(x,y)
r3=r1.greater(r2)
r3.display()




class student:
  def __init__(self,rollno,name):
    self.rollno=rollno
    self.name=name
  def putdata(self):
    print(self.rollno,self.name)
    
class test(student):
  def __init__(self,rollno,name,mt1,mt2):
    super().__init__(rollno,name)
    self.mt1=mt1
    self.mt2=mt2
  def putmarks(self):
    self.putdata()
    print("Mt1 is:",self.mt1)
    print("Mt2 is:",self.mt2)
    
class result(test):
  def __init__(self,rollno,name,mt1,mt2):
    super().__init__(rollno,name,mt1,mt2)
  def putresult(self):
    self.putmarks()
    print("total marks are:",(self.mt1+self.mt2))

s=result(102,"Harsh",100,200)
s.putresult()





class student:
  def __init__(self,rollno,name):
    self.rollno=rollno
    self.name=name
  def putdata(self):
    print(self.rollno,self.name)
class test:
  def __init__(self,mt1,mt2):
    self.mt1=mt1
    self.mt2=mt2
  def putmarks(self):
    print("Mt1 is:",self.mt1)
    print("Mt2 is:",self.mt2)
class result(student,test):
  def __init__(self,rollno,name,mt1,mt2):
    student.__init__(self,rollno,name)
    test.__init__(self,mt1,mt2)
  def putresult(self):
    self.putdata()
    self.putmarks()
    print("total marks are:",(self.mt1+self.mt2))

s=result(102,"Harsh",100,200)
s.putresult()


class first:
  def getdata(self,a):
    self.a=a
  def putdata(self):
    print(self.a)

class second(first):
  
  def square(self):
    self.sq=(self.a)*self.a
    print("square is",self.sq)
class third(second):

  def cube(self):
    self.cb=self.sq*self.a
    print("cube is:",self.cb)

c=third()
c.getdata(2)
c.square()
c.cube()
    
class first:
  def getdata(self,a):
    self.a=a
  def putdata(self):
    print(self.a)

class second(first):
  
  def square(self):
    self.sq=(self.a)*self.a
    print("square is",self.sq)

class third(second):

  def cube(self):
    self.cb=self.a**3
    print("cube is:",self.cb)

c=third()
c.getdata(2)
c.cube()


class first:
  def getdata(self,a):
    self.a=a
  def putdata(self):
    print(self.a)

class second(first):
  
  def square(self):
    self.sq=(self.a)*self.a
    print("square is",self.sq)

class third(first):

  def cube(self):
    self.cb=self.a**3
    print("cube is:",self.cb)

c=third()
b=second()
c.getdata(2)
c.cube()
b.getdata(2)
b.square()


class sample:
  ctr=5
  def __init__(self,num):
    self.num=num
    print(sample.ctr)
    
s=sample(10)
print(s.ctr)
print(s.num)
print(dir(s))
print(dir(sample))
p=sample(20)
print(p.ctr)
print(p.num)
print(p.__dict__)
s.ctr=100
print(s.ctr)
print(p.ctr)
print(sample.ctr)
sample.ctr=6
print(sample.ctr)
print(s.ctr)
print(p.ctr)
q=sample(30)
print(q.ctr)
print(q.num)
sample.ctr=10
print(s.ctr,p.ctr,q.ctr)



class room:
  pass
r=room()
r.l=10
r.__setattr__('b',20)
print(r.__dict__)
print(r.l,r.__getattribute__('b'))
r.h=30
print(r.__dict__)
del r.h
r.__delattr__('b')
print(r.__dict__)


class number:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def display(self):
    print(self.a,self.b)
class demo:
  def swap(n):
    temp=n.a
    n.a=n.b
    n.b=temp
  def main():
    nobj=number(10,20)
    nobj.display()
    demo.swap(nobj)
    nobj.display()

demo.main()



class alpha:
  def display():
    print("display of alpha ex:")
class beta(alpha):
  def showbeta():
    print("show of beta ex:")
  def display():
    alpha.display()
    print("display of beta ex:")
 
class gamma(alpha):
  def showgamma():
    print("show of gamma ex")
class demo(beta,gamma):
  def show():
    print("Show of demo ex")
print(dir(demo))
demo.display()
demo.showbeta()
demo.showgamma()
demo.show()



class alpha:
  def display():
    print("display of alpha ex")
class beta:
  def display():
    print("display of beta ex")
class gamma(alpha,beta):
  def show():
    alpha.display()
    beta.display()
    print("Show of gamma ex")
gamma.show()



class rectangle:
  nos_ins=0
  def __init__(self):
    rectangle.nos_ins=rectangle.nos_ins+1

  def show(self):
    print(rectangle.nos_ins)
    
  @staticmethod
  def printdata():
    print(rectangle.nos_ins)

  @classmethod
  def display(cls):
    print(cls.nos_ins)

r=rectangle()
r.display()
rectangle.display()
r.show()
rectangle.show()
r.printdata()
rectangle.printdata()
