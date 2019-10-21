for letter in "python":
  print(letter)

for item in[1,2,3,4]:
  print(item)
  
d={"name":"Harsh","age":"20"}
for item in d:
  print (item)

d={"name":"Harsh","age":"20"}
for key in d:
  print(key,"",d[key])

print (list(range(5)))

print (list(range(1,11)))

print (list(range(2,12,2)))

print (list(range(10,0,-1)))

l=[10,20,30,40]
for i in range(len(l)):
  print(l[i])
  print("item at",0,"index is",l[i])

l=[10,20,30,40,50]
for index,item in enumerate(l):
  print("item at",index,"index is",item)

s="python"
print(s[::-1])

s="python"
rev=""
for c in s:
  rev=c+rev
  print(rev)

s="python"
rev=""
for i in range(len(s)-1,-1,-1):
               rev=rev+s[i]
               print(rev)

l=[10,20,30]
x=list(enumerate(l))
print(x)

for i in range(1,6):
  print()
  for j in range(1,6):
    print(j,end='')
    
for i in range(1,6):
  print()
  for j in range(1,6):
   print(i,end='')

flag=0
n=int(input("enter any no.:"))
for i in range(2,n//2+1):
  if n%i==0:
    flag=1
    break

if flag==0:
  print("prime")
else:
  print("not prime")

for i in range(1,6):
  print()
  for j in range(1,i+1):
    print(j,end='')

for i in range(5,0,-1):
  print()
  for j in range(1,i+1):
    print(j,end='')

for i in range(1,6):
  print()
  for j in range(5,i-1,-1):
    print(j,end='')

for i in range(1,6):
  print()
  for j in range(i,6,+1):
   print(j,end='')

for i in range(5,0,-1):
  print()
  for j in range(i,6):
    print(j,end='')

for i in range(5,0,-1):
  print()
  for j in range(i,0,-1):
    print(j,end='')

for i in range(1,6):
  print()
  for j in range(i,0,-1):
    print(j,end='')
