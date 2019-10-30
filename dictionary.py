d={"name":"harsh","age":25}
print(d)
d={}
d["course"]="pgdca"
d[5]=200
d[("Maths","Science")]=(90,60)
d["course"]="PGDCA"
print(d)


d={"name":"harsh","age":25}
d["name"]="Rama"
print(d)

d={"name":"harsh","age":25}
d["course"]="PGDCA"
print(d)
d["course"]="MCA"
print(d)

word='hello'
d=dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)

d={"name":"harsh","age":25}
for key in d:
    print(key,':',d[key])
    print(d.keys())
    print(d.values())

d={"name":"harsh","age":25}
for key,value in d.items():
    print(key,':',value)

d={"name":"harsh","age":25}
print(d)
print(str(d))
print(type(d))

d={"name":"harsh","age":25}
print(d.items())

d=[("apple",120),("mango",50),("banana",80)]
d=dict(t)
print(d)

d1={"name":"harsh","age":25}
d2={"poem":9068852215}
d1.update(d2)
print(d1)

d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
    print(d4)

t=[("apple",120),("mango",50),("banana",80)]
d=dict(t)
print(d)

t1=("name","age")
t2=("Ram",20)
d={}
d=d.fromkeys(t1)
i=0
for key in d:
  d[key]=t2[i]
  i=i+1
print(d)

t1=("name","age")
t2=("ram",20)
d={}
d=dict(zip(t1,t2))
print(d)

d={"name":"harsh","age":25}
print(d.get("name"))
print(d.get("phone"))
print(d.get("phone",0))
print(d[phone])

word="hello"
d={}
for c in word:
  d[c]=d.get(c,0)+1
print(d)

d={"pooja":80,"Aman":50,"seema":70}
print(sorted(d))
print(sorted(d.items()))
print(sorted(d.items(),key=lambda t:t[-1]))

students={"ram":(80,30,30),"amit":(60,70,90),"mohan":(50,40,60)}
print(sorted(students.items(),key=lambda t:t[1][-1],reverse=True))

students={"ram":(80,30,30),"amit":(60,70,90),"mohan":(50,40,60)}
print(students)
k=students.keys()
x=list(map(lambda t:tuple(sorted(t)),students.values()))
d=dict(zip(k,x))
print(d)


s={}
d={"ram":(80,30,30),"amit":(60,70,90),"mohan":(50,40,60)}
for key in d:
  s[key]=sorted(d[key])

print(s)


l1=[1,2,3]
l2=[3,4,5]

l=[l1[i]+l2[i] for i in range(len(l1))]
print(l)

print(list(map(lambda x,y:x+y,l1,l2)))



l=[i for i in range(1,21) if i%2==0 and i%5==0]
print(l)
