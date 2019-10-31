file=open("friends.txt","a")
reply="y"
while reply=="y":
  name=input("Eneter any name:")
  name=name+"\n"
  file.write(name)
  reply=input("Add more name y or n?")

file.close()

file=open("friends.txt","r")
content=file.read()
print(content)
file.close

file=open("friends.txt","r")
line=file.readline()
while line!='':
  print(line,end="")
  line=file.readline()
file.close()

file=open("friends.txt","r")
datalist=file.readlines()
print(datalist)
for line in datalist:
  print(line,end="")
file.close()


import os
print(os.getcwd())
print(os.listdir(os.getcwd()))


file=open("friends.txt","a")
l=["Harsh","Vedantika","mehak"]
file.writelines(l)
file.close()


file=open("friends.txt","r")
ctr=0
datalist=file.readlines()
for line in datalist:
  ctr=ctr+1
  print(ctr,":",line,end="")
file.close()


newdata=input("Enter updated record:")
newlist=newdata.split(",")
f=open("friends.txt","r")
t=open("temp.txt","w")
line=f.readline()
while line!="":
  l=line.split(",")
  if (l[0]==newlist[0]):
    t.write(newdata+"\n")
  else:
    t.write(line)
  line=f.readline()
f.close()
t.close()
import os
os.remove("friends.txt")
os.rename("temp.txt","friends.txt")
for line in open("friends.txt"):
  print(line)




file=open("student.txt","a")
reply="y"
while reply=="y":
  name=input("Enter the name:")
  name=name+"\n"
  file.write(name)
  reply=input("add more name y or n?")

file.close()
  

file=open("student.txt","r")
datalist=file.readlines()
for line in datalist:
  print(line,end="")
file.close


newdata=input("Enter updated record:")
newlist=newdata.split(",")
f=open("student.txt","r")
t=open("temp.txt","w")
line=f.readline()
while line!="":
  l=line.split(",")
  if (l[0]==newlist[0]):
    t.write(newdata+"\n")
  else:
    t.write(line)
  line=f.readline()
f.close()
t.close()
import os
os.remove("student.txt")
os.rename("temp.txt","student.txt")
for line in open("student.txt"):
  print(line)


rollno=input("Enter the roll no to search")
f=open("friends.txt")
line=f.readline()
while line!="":
  print(line)
  if (line.strip()==rollno):
    print(line,end="")
    break
  line=f.readline()
f.close()



newdata=input("Enter updated record:")
newlist=newdata.split(",")
f=open("student.txt","r")
templist=[]
datalist=f.readlines()
for line in datalist:
  l=line.split(",")
  if(l[0]==newlist[0]):
    templist.append(newdata+"\n")
  else:
    templist.append(line)
f.close()

f=open("student.txt","w")
f.writelines(templist)
f.close()
for line in open("student.txt"):
  print(line,end="")
