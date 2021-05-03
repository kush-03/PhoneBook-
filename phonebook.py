from tkinter import *
from tkinter.messagebox import *
# Code to add widget will go here……..
from demo1 import *
import sqlite3
con=sqlite3.Connection("phonebook")
cur=con.cursor()
cur.execute("create table if not exists contact_infor(contact_id integer primary key AUTOINCREMENT,fname varchar(20),lname varchar(20),company varchar(20),address varchar(20),city varchar(20),pincode number,website varchar(20),dob date)")
cur.execute("create table if not exists phone_infor(contact_id integer,phone_type varchar(20),phone_num number(20),foreign key(contact_id) references contact_infor(contact_id)on delete cascade)")
cur.execute("create table if not exists email_infor(contact_id integer,email_type varchar(20),email_id varchar(20),foreign key(contact_id) references contact_infor(contact_id)on delete cascade)")
root=Tk()
root.title("Phonebook")
root.geometry("500x630")
root.configure(background="violet")
a=PhotoImage(file='573816.gif')
Label(root,image=a).place(x=180,y=1)

Label(root,text='PHONEBOOK',bg='yellow',font=('aerial bold',14),fg='black').place(x=190,y=154)

Label(root,text='First name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=200)
e1=Entry(root)
e1.place(x=190,y=200)


Label(root,text='last name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=230)
e2=Entry(root)
e2.place(x=190,y=230)


Label(root,text='company name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=260)
e3=Entry(root)
e3.place(x=190,y=260)


Label(root,text='address',bg='white', fg='black',font=('aerial',10)).place(x=70,y=290)
e4=Entry(root)
e4.place(x=190,y=290)


Label(root,text='city',bg='white', fg='black',font=('aerial',10)).place(x=70,y=320)
e5=Entry(root)
e5.place(x=190,y=320)


Label(root,text='pincode',bg='white', fg='black',font=('aerial',10)).place(x=70,y=350)
e6=Entry(root)
e6.place(x=190,y=350)


Label(root,text='website',bg='white', fg='black',font=('aerial',10)).place(x=70,y=380)
e7=Entry(root)
e7.place(x=190,y=380)


Label(root,text='DOB',bg='white', fg='black',font=('aerial',10)).place(x=70,y=410)
e8=Entry(root)
e8.place(x=190,y=410)


Label(root,text='Select Phone Type',bg='violet',fg='indigo',font=('aerial bold',16)).place(x=20,y=440)
v1=IntVar()
r1=Radiobutton(root,text='office',variable=v1,value=1,fg='black',bg='violet',font=('aerial ',8)).place(x=220,y=440)
r2=Radiobutton(root,text='home',variable=v1,value=2,fg='black',bg='violet',font=('aerial',8)).place(x=280,y=440)
r3=Radiobutton(root,text='Personal',variable=v1,value=3,fg='black',bg='violet',font=('aerial',8)).place(x=340,y=440)
if v1.get()==1:
    c='office'
elif v1.get()==2:
    c='home'
else:
    c='Personal'
Label(root,text='Phone number',fg='black',bg='white',font=('aerial',10)).place(x=50,y=470)
e9=Entry(root)
e9.place(x=190,y=470)


Label(root,text='Select E-mail Type',bg='violet',fg='indigo',font=('aerial bold',16)).place(x=20,y=500)
v2=IntVar()
Radiobutton(root,text='office',variable=v2,value=1,fg='black',bg='violet',font=('aerial',8)).place(x=220,y=500)
Radiobutton(root,text='personal',variable=v2,value=2,fg='black',bg='violet',font=('aerial',8)).place(x=280,y=500)
if v2.get()==1:
    d='office'
else :
    d='personal'   
Label(root,text='Email id',fg='black',bg='white',font=('aerial',10)).place(x=50,y=530)
e10=Entry(root)
e10.place(x=190,y=530)




def close(e=1):
    root.destroy()
Button(root,text='close',fg='black',command=close).place(x=360,y=580)


def save():
    cur.execute("insert into contact_infor(fname,lname,company,address,city,pincode,website,dob)values(?,?,?,?,?,?,?,?)",(str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get()),str(e7.get()),str(e8.get())))
    cur.execute("insert into phone_infor(contact_id,phone_type,phone_num)values((select max(contact_id) from contact_infor),?,?)",(c,str(e9.get())))
    cur.execute("insert into email_infor(contact_id,email_type,email_id)values((select max(contact_id) from contact_infor),?,?)",(d,str(e10.get())))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    showinfo('saved','record successfully saved')
Button(root,text='save',fg='black',command=save).place(x=120,y=580)


def search():
    root=Tk()
    root.geometry("500x630")
    root.title('search')
    root.configure(background='purple')
    Label(root,text='SEARCHING PHONEBOOK',fg='black',font=('aerial bold',18)).place(x=100,y=0)
    Label(root,text='Enter Name',fg='black',bg='purple',font=('aerial bold',14)).place(x=50,y=60)
    f=Entry(root)
    f.place(x=210,y=60)
    cur.execute("select fname,lname from contact_infor order by fname")
    fetch=cur.fetchall()
    lb=Listbox(root,width=70,height=30)
    lb.place(x=140,y=90)
    for i in fetch:
        lb.insert(END,i)
    con.commit()
    
    def fun(e=1):
        b=[1]
        b[0]=['%'+f.get()+'%']
        lb.delete(0,END)
        cur.execute("select fname,lname from contact_infor where fname like ? order by fname",b[0])
        data=cur.fetchall()
        for i in data:
            lb.insert(END,i)
        con.commit()
    root.bind('<Key>',fun)
    
    def onselect(e=1):
        clicked_item=lb.curselection()
        c_n=lb.get(clicked_item)
        cur.execute("select contact_id from contact_infor where fname=(?) and lname=(?)",(c_n[0],c_n[1]))
        m= cur.fetchall()
        for i in m:
            for j in i:
                i_d= j
        lb1=Listbox(root,width=70,height=30)
        lb1.place(x=140,y=90)
        cur.execute("select fname,lname,company,address,city,pincode,website,dob,phone_num,email_id from contact_infor ci inner join phone_infor p on ci.contact_id=p.contact_id inner join email_infor e on ci.contact_id=e.contact_id where ci.contact_id=(?)",(i_d,))
        g=cur.fetchall()
        c=0
        lis=['fname','lname','company','address','city','pincode','website','dob','phone_num','email_id'] 
        for i in g:
            for j in i:
                lb1.insert(c,str(lis[c])+' : '+'  ' + str(j))
                c=c+1
                
        def delete():
            cur.execute("delete from contact_infor where contact_id=(?)",(i_d,))
            con.commit()
            showinfo("delete","contact deleted")    
        Button(lb1,text='delete',command=delete).place(x=180,y=400)

        
        def func(e=1):
            lb1.destroy()
        Button(lb1,text='back',command=func).place(x=80,y=400)

        def edit():
            root=Tk()
            root.geometry("400x380")
            root.configure(background='sky blue')
            root.title("Edit")
            for i in g:
                print (i)

            Label(root,text='First name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=20)
            e1=Entry(root)
            e1.insert(END,i[0])
            e1.place(x=190,y=20)


            Label(root,text='last name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=50)
            e2=Entry(root)
            e2.insert(END,i[1])
            e2.place(x=190,y=50)


            Label(root,text='company name',bg='white', fg='black',font=('aerial',10)).place(x=70,y=80)
            e3=Entry(root)
            e3.insert(END,i[2])
            e3.place(x=190,y=80)


            Label(root,text='address',bg='white', fg='black',font=('aerial',10)).place(x=70,y=110)
            e4=Entry(root)
            e4.insert(END,i[3])
            e4.place(x=190,y=110)


            Label(root,text='city',bg='white', fg='black',font=('aerial',10)).place(x=70,y=140)
            e5=Entry(root)
            e5.insert(END,i[4])
            e5.place(x=190,y=140)


            Label(root,text='pincode',bg='white', fg='black',font=('aerial',10)).place(x=70,y=170)
            e6=Entry(root)
            e6.insert(END,i[5])
            e6.place(x=190,y=170)


            Label(root,text='website',bg='white', fg='black',font=('aerial',10)).place(x=70,y=200)
            e7=Entry(root)
            e7.insert(END,i[6])
            e7.place(x=190,y=200)


            Label(root,text='DOB',bg='white', fg='black',font=('aerial',10)).place(x=70,y=230)
            e8=Entry(root)
            e8.insert(END,i[7])
            e8.place(x=190,y=230)

            Label(root,text='Phone num',fg='black',bg='white',font=('aerial',10)).place(x=70,y=260)
            e9=Entry(root)
            e9.insert(END,i[8])
            e9.place(x=190,y=260)

            Label(root,text='Email id',fg='black',bg='white',font=('aerial',10)).place(x=70,y=290)
            e10=Entry(root)
            e10.insert(END,i[9])
            e10.place(x=190,y=290)

            def back_fun():
                root.destroy()
            Button(root,text='BACK',command=back_fun).place(x=280,y=340)

            def update():
                for i in m:
                    for j in i:
                        i_d=j
                cur.execute("update contact_infor set fname=(?),lname=(?),company=(?),address=(?),city=(?),pincode=(?),website=(?),dob=(?) where contact_id=(?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),i_d))
                con.commit()
                cur.execute('update phone_infor set phone_num=(?) where contact_id=(?)',(str(e9.get()),i_d))
                con.commit()
                cur.execute('update email_infor set email_id=(?) where contact_id=(?)',(str(e10.get()),i_d))
                con.commit()
                showinfo('update','contact updated')              
            Button(root,text='UPDATE',command=update).place(x=340,y=340)  
        Button(lb1,text='edit',fg='black',command=edit).place(x=280,y=400)   
    lb.bind('<<ListboxSelect>>',onselect)



    
    def close(e=1):
        root.destroy()
    Button(root,text='close',fg='black',command=close).place(x=240,y=590)
    
Button(root,text='search',fg='black',command=search).place(x=240,y=580)  
root.mainloop()
    
