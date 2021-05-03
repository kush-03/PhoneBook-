from tkinter import *  
root = Tk()  
# Code to add widget will go here……..  
root.configure(background='pink')
root.geometry('400x280')
Label(root,text='Project title: PHONEBOOK',fg='black',font=('times new roman bold',18)).place(x=1,y=0)
Label(root,text='Project of python and database',fg='black',font=('times new roman bold',18)).place(x=60,y=60)
Label(root,text='DEVELOPED BY:',fg='black',font=('times new roman bold',18)).place(x=110,y=100)
Label(root,text='KUSH AGARWAL',fg='BLUE',font=('aerial bold',18)).place(x=120,y=140)
Label(root,text='Enroll No:181B114',fg='BLUE',font=('aerial bold',18)).place(x=120,y=180)

def close(e=1):
    root.destroy()

root.bind('<Motion>',close)
root.mainloop()  
