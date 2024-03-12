import tkinter as kt
from tkinter import *
from tkinter import messagebox
window=kt.Tk()
window.title("Calculator")
frame=kt.Frame(window,padx=10)
frame.pack()
val=kt.Entry(frame,borderwidth=3,width=35)
val.grid(columnspan=3,ipady=2,pady=2)
def call(number):
    val.insert(kt.END,number)
def same():
        y=str(eval(val.get()))
        val.delete(0,kt.END)
        val.insert(0,y)
def clear():
    val.delete(0,kt.END)
btn1=kt.Button(frame,text='7',padx=15,pady=5,width=3,command=lambda:call(7))
btn1.grid(row=1,column=0,pady=2)         
btn2=kt.Button(frame,text='8',padx=15,pady=5,width=3,command=lambda:call(8))
btn2.grid(row=1,column=1,pady=2) 
btn3=kt.Button(frame,text='9',padx=15,pady=5,width=3,command=lambda:call(9))
btn3.grid(row=1,column=2,pady=2)  
btn4=kt.Button(frame,text='*',padx=15,pady=5,width=3,command=lambda:call('*'))
btn4.grid(row=1,column=3,pady=2) 
btn5=kt.Button(frame,text='4',padx=15,pady=5,width=3,command=lambda:call(4))
btn5.grid(row=2,column=0,pady=2)
btn6=kt.Button(frame,text='5',padx=15,pady=5,width=3,command=lambda:call(5))
btn6.grid(row=2,column=1,pady=2)  
btn7=kt.Button(frame,text='6',padx=15,pady=5,width=3,command=lambda:call(6))
btn7.grid(row=2,column=2,pady=2) 
btn8=kt.Button(frame,text='/',padx=15,pady=5,width=3,command=lambda:call('/'))
btn8.grid(row=2,column=3,pady=2)  
btn9=kt.Button(frame,text='1',padx=15,pady=5,width=3,command=lambda:call(1))
btn9.grid(row=3,column=0,pady=2)   
btu1=kt.Button(frame,text='2',padx=15,pady=5,width=3,command=lambda:call(2))
btu1.grid(row=3,column=1,pady=2) 
btu2=kt.Button(frame,text='3',padx=15,pady=5,width=3,command=lambda:call(3))
btu2.grid(row=3,column=2,pady=2) 
btu3=kt.Button(frame,text='+',padx=15,pady=5,width=3,command=lambda:call('+'))
btu3.grid(row=3,column=3,pady=2)  
btu4=kt.Button(frame,text='c',padx=15,pady=5,width=3,command=clear)
btu4.grid(row=4,column=0,pady=2) 
btu5=kt.Button(frame,text='=',padx=15,pady=5,width=8,command=same)
btu5.grid(row=4,column=1,pady=2) 
btu6=kt.Button(frame,text='-',padx=15,pady=5,width=3,command=lambda:call('-'))
btu6.grid(row=4,column=2,pady=2)  
window.mainloop()                                           