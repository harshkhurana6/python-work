import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

l=[10,20,30,40,50]
s=pd.Series(l)
print(s)


d={"Name":"Harsh","Age":25}
s=pd.Series(d)
print(s)
print(s.index)


l1=[10,20,30]
l2=["Jan","Feb","Mar"]
s=pd.Series(l1,index=l2)
print(s)

d={"Ecode":[1001,1002,1003],
   "Ename":["Harsh","Shivam","Surya"],
   "Salary":[20000,30000,40000]}
df=pd.DataFrame(d,index=["i","ii","iii"])
print(df)


d={'x':{'p':1,'q':2},'y':{'p':3,'q':4}}
df=pd.DataFrame(d)
print(df)


arr=np.arange(10).reshape(2,5)
df=pd.DataFrame(arr,index=["a","b"],columns=["one","two","three","fours","five"])
print(df)
print(df.size,df.shape)
print(df.T)


d={"Ecode":[1001,1002,1003],
   "Ename":["Harsh","Shivam","Surya"],
   "Salary":[20000,30000,40000]}
df=pd.DataFrame(d,index=["i","ii","iii"])
print(df)
print()
print()
print(df[["Ecode","Salary"]])
print(df.loc['i',"Ename"])
print(df.Ename['i'])

print()
print()

for (row,rowseries) in df.iterrows():
    print("Row index:",row)
    print("Containing:")
    print(rowseries)

print()
print()
for (col,colseries) in df.iteritems():
    print("Column index:",col)
    print("Containing:")
    print(colseries)

print(df.describe())
print(df.cumsum())

a=np.arange(500,360,-10)
print(a)

x=np.arange(1,6)
y=np.log(x)
plt.bar(x,y,color='r')
plt.xlabel="Categories"
plt.ylabel="Value Series"
plt.title("My first plot")
plt.show()

d={"Ecode":[1001,1002,1003],
    "Ename":["Harsh","Shivam","Surya"],
    "Salary":[20000,30000,40000]}
df=pd.DataFrame(d)
print(df)
print(df.var())
print(df.iloc[0])
df2=df.mean(axis=1)
print(df2)



d={"Year":[1991,1991,1991,1991,1991,1991,1991,1991,1991,1992,1992,1992,1992,1992,1992,1992,1992,1992],
  "Month":["Jan","Jan","Jan","Feb","Feb","Feb","Mar","Mar","Mar","Jan","Jan","Jan","Feb","Feb","Feb","Mar","Mar","Mar"],
   "Ecode":[1001,1002,1003,1001,1002,1003,1001,1002,1003,1001,1002,1003,1001,1002,1003,1001,1002,1003],
   "Ename":["Ram","sham","Mohan","Ram","sham","Mohan","Ram","sham","Mohan","Ram","sham","Mohan","Ram","sham","Mohan","Ram","sham","Mohan"],
   "Salary":[20000,30000,40000,22000,32000,42000,25000,35000,45000,20000,30000,40000,22000,32000,42000,25000,35000,45000]}
df=pd.DataFrame(d)
print(df)
df1=df.pivot_table(index="Ecode",columns="Ename",values="Salary")
print(df1)
df1=df.pivot_table(index=["Year","Month"],columns="Ename",values="Salary")
print(df1)
print(df.sort_values(by="Salary",ascending=False))
print(df.sort_values(by=["Year","Ename"],ascending=False))
df1=df.reindex(["Ecode","Ename","Salary","Year","Month"],axis=1)
print(df1)
##or
df1=df.reindex(columns=["Ecode","Ename","Salary","Year","Month"])
print(df1)

df1=df.groupby(by="Year")
print(df1.groups)
print(df1.get_group(1991).count(),df1.get_group(1991).size)

df1=df.groupby(by=["Year","Month"])
print(df1.groups)
print(df1.get_group((1991,"Feb")))
df.hist(column="Salary")
plt.bar(df.Ename,df.Salary)
plt.show()
