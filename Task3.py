import tkinter as kt
from tkinter import *
import random
import string
from tkinter import messagebox
window=kt.Tk()
window.geometry('500x450+500+200')
window.title("Password Generator")
window.resizable(False,False)
def generate_password():
    length=int(character_length.get())
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(length))
    blank.insert(length,password)
def clear():
    blank.delete(0,kt.END)
def clean():
    messagebox.showinfo("showinfo","Accepted")
    blank.delete(0,kt.END)
    name.delete(0,kt.END)
    character_length.delete(0,kt.END)
passwordLabel=Label(window,text="Password Generator",font=('Times New Roman',20,'bold'),fg="navyblue")
passwordLabel.pack()
user=Label(window,text="Enter User Name:",font=('Times New Roman',10,'bold'),pady=10)
user.pack()
name=Entry(window,font=('Times New Roman',10,'bold'),width=30)
name.pack()
label_characters=Label(window,text="Enter Password Length:",font=('Times New Roman',10,'bold'),pady=10)
label_characters.pack()
character_length=Entry(window,font=('Times New Roman',10,'bold'),width=30)
character_length.pack()
Gen=Label(window,text="Generated Password:",font=('Times New Roman',10,'bold'),pady=10)
Gen.pack()
blank=Entry(window,font=('Times New Roman',10,'bold'),width=30)
blank.pack()
btn1=Button(window,text='GENERATE PASSWORD',font=('Times New Roman',15,'bold'),fg='white',bg='navyblue',cursor="hand2",command=generate_password)
btn1.pack(pady="30px")
btn2=Button(window,text='ACCEPT',font=('Times New Roman',13,'bold'),fg="navyblue",bg="white",command=clean)
btn2.pack(pady="5px")
btn3=Button(window,text='RESET',font=('Times New Roman',13,'bold'),fg="navyblue",bg="White",command=clear)
btn3.pack()
window.mainloop()