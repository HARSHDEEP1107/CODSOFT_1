import tkinter as kt
from tkinter import *
from tkinter import messagebox
def newTask():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","Please enter some task")

def deleteTask():
    lb.delete(ANCHOR)
window=kt.Tk()
window.title("To Do List Application")
window.geometry('500x450+500+200')
window.config(bg='cyan')
window.resizable(width=False,height=False)
frame=Frame(window)
frame.pack(pady=10)
lb=Listbox(frame,width=25,height=8,font=('Times',18),bd=0,fg='#464646',selectbackground='#a6a6a6', activestyle="none")
lb.pack(side=LEFT,fill=BOTH)
task_list=['Playing','Exercise','Focus on Studies']
for item in task_list:
    lb.insert(END,item)
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview) 

my_entry=Entry(window,font=('Times',15))
my_entry.pack(pady=20)
button_frame=Frame(window)
button_frame.pack(pady=20)

btn=Button(button_frame,text='Add Task',font=('Times',14),bg='Yellow',padx=20,pady=10,command=newTask)
btn.pack(fill=BOTH,expand=True,side=LEFT)

quick=Button(button_frame,text='Delete Task',font=('Times',14),bg='#ff8b61',padx=20,pady=10,command=deleteTask)
quick.pack(fill=BOTH,expand=True,side=LEFT)

window.mainloop()

