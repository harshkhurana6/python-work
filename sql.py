
inserting data and creating table

from tkinter import *
import sqlite3
window=Tk()
window.title("STOCK ENTERY SCREEEN")
window.geometry("350x200")
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt4=StringVar()

l=Label(window,text="STOCK ENTERY SCREEEN")
l.place(x=100,y=0)
l1=Label(window,text="Item Code:")
l1.place(x=0,y=30)
l2=Label(window,text="Item Name:")
l2.place(x=0,y=60)
l3=Label(window,text="Rate:")
l3.place(x=0,y=90)
l4=Label(window,text="QIH:")
l4.place(x=0,y=120)


t1=Entry(window,textvariable=txt1)
t1.place(x=150,y=30)
t2=Entry(window,textvariable=txt2)
t2.place(x=150,y=60)
t3=Entry(window,textvariable=txt3)
t3.place(x=150,y=90)
t4=Entry(window,textvariable=txt4)
t4.place(x=150,y=120)

def button_clear():
    txt1.set("")
    txt2.set("")
    txt3.set("")
    txt4.set("")
    t1.focus()

def button_insert():
    sqlite_file='inventory.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute('create table if not exists stock(icode Text,iname Text,rate Text,QIH Text)')
    c.execute('insert into stock(icode,iname,rate,QIH) values (?,?,?,?)',(txt1.get(),txt2.get(),txt3.get(),txt4.get()))
    conn.commit()
    button_clear()

b1=Button(text="Clear",command=button_clear)
b2=Button(text="Insert",command=button_insert)
b3=Button(text="Exit",command=window.destroy)

b1.place(x=150,y=150)
b2.place(x=0,y=150)
b3.place(x=300,y=150)
t1.focus()
window.mainloop()

exctracting data

import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
c.execute('Select * from stock')
data=c.fetchall()
print(data)

for row in data:
    print("Item Code:",row[0],"Item Name:",row[1],"Rate:",row[2],"QIH:",row[3])
conn.commit()
conn.close()


changing data

import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
icode="1001"
iname1="shirt"
rate1="700"
QIH1="3"
c.execute("update stock set iname=(?),rate=(?),QIH=(?) where icode=(?)",(iname1,rate1,QIH1,icode))
conn.commit()
conn.close()

deleting data


import sqlite3
sqlite_file='inventory.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
icode="1001"
c.execute("delete from stock where icode=(?)",(icode,))
c.execute('Select * from stock')
data=c.fetchall()
print(data)
for row in data:
    print("Icode:",row[0],"iname:",row[1],"Rate:",row[2],"QIH:",row[3])

conn.commit()
conn.close()


import sqlite3
from employee import Employee
conn=sqlite3.connect(':memory:')
c=conn.cursor()
c.execute("""CREATE TABLE employees(first text, last text, pay interger)""")
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees where last=:last",{'last':lastname})
    return c.fetchall()

    
def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first =:first AND last=:last""",
                  {'first':emp.first,'last':emp.last,'pay':pay})
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first =:first AND last=:last",
                  {'first':emp.first,'last':emp.last,'pay':emp.pay})

emp_1=Employee('John','Doe',80000)
emp_2=Employee('Jane','Doe',90000)
insert_emp(emp_1)
insert_emp(emp_2)
emps=get_emps_by_name('Doe')
print(emps)
update_pay(emp_2,95000)
remove_emp(emp_1)
emps=get_emps_by_name('Doe')
print(emps)
conn.close()
