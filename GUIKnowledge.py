from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

def check_time_now():
    text = datetime.now().strftime('%D%M %H:%M:%S')
    messagebox.showinfo('check time now',text)
B1 = ttk.Button(GUI, text='check datetime now',command=check_time_now)
B1.pack(ipadx=20,ipady=20)

def subject():
    text =' mon 11.10-13.40 and fri 13.00-15.30'
    messagebox.showinfo('study',text)

FB1 = Frame(GUI)
FB1.place(x=300,y=100)
B2 = ttk.Button(FB1, text='study',command=subject)
B2.pack(ipadx=20,ipady=20)

def age():
    birth = "27-11-2003"
    birthday = datetime.strptime(birth, "%d-%m-%y")
    text = datetime.now()- birthday
    messagebox.showinfo('age now',text)

FB1 = Frame(GUI)
FB1.place(x=300,y=200)
B2 = ttk.Button(FB1, text='age now',command=age)
B2.pack(ipadx=20,ipady=20)

def last_update():
    text = '02/10/23'
    messagebox.showinfo('last_update',text)

FB1 = Frame(GUI)
FB1.place(x=300,y=300)
B2 = ttk.Button(FB1, text='last updated',command=last_update)
B2.pack(ipadx=20,ipady=20)

def money():
    text = ' ตอนนี้เงินรวม 10,000 THB'
    messagebox.showinfo('money',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1, text='money',command=money)
B2.pack(ipadx=20,ipady=20)

def weight():
    text = ' ตอนนี้น้ำหนัก 52 K(g)'
    messagebox.showinfo('weight',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1, text='weight',command=weight)
B2.pack(ipadx=20,ipady=20)

def height():
    text = ' ล่าสุดส่วนสูง 172 C(m)'
    messagebox.showinfo('weight',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=200)
B2 = ttk.Button(FB1, text='height',command=height)
B2.pack(ipadx=20,ipady=20)



GUI.mainloop()
