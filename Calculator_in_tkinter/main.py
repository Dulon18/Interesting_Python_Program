# pip install tkinter

import tkinter as tk
from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Calculator in Python")
root.iconbitmap('cal.ico')
root.maxsize(width=340,height=475)
root.minsize(width=340,height=475)

var=tk.StringVar()
entry=Entry(root,state='readonly',textvariable=var,font=('Arial',16,'bold'),bg="#26004d",bd=10).grid(rowspan=1,columnspan=100,ipadx=35,ipady=10)
#root.config(bd=25)
root.config(bg='#26004d')

#.............Function Start...........

operator=""

def press(num):
    global operator
    operator+= str(num)
    var.set(operator)

def clear():
    global operator
    operator =" "
    var.set(operator)

def Equal():
    global operator
    equ=str(eval(operator))
    var.set(equ)
    operator = " "
    
#.............Function End...........
    
#.............1st Row............

bracket =Button(root,text=' ( ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('(')).grid(row=1,column=0,ipadx =10, ipady=10)
bracket1 = Button(root,text=' ) ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press(')')).grid(row=1,column=1,ipadx =10, ipady=10)
percent = Button(root,text=' % ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('%')).grid(row=1,column=2,ipadx =10, ipady=10)
ac = Button(root,text='AC',bg='yellow',bd=12,font=('Arial',16,'bold'),command=clear).grid(row=1,column=3,ipadx =10, ipady=10)

#..........2nd Row...................

seven =Button(root,text='7',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('7')).grid(row=2,column=0,ipadx =10, ipady=10)
eight = Button(root,text='8',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('8')).grid(row=2,column=1,ipadx =10, ipady=10)
nine = Button(root,text=' 9 ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('9')).grid(row=2,column=2,ipadx =10, ipady=10)
div= Button(root,text='  / ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('/')).grid(row=2,column=3,ipadx =10, ipady=10)

#>>>>>>>>>>3rd row<<<<<<<<<<<<<<<

four = Button(root,text='4',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('4')).grid(row=3,column=0,ipadx =10, ipady=10)
five = Button(root,text='5',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('5')).grid(row=3,column=1,ipadx =10, ipady=10)
six = Button(root,text=' 6 ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('6')).grid(row=3,column=2,ipadx =10, ipady=10)
mult = Button(root,text=' x ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('*')).grid(row=3,column=3,ipadx =10, ipady=10)

#<<<<<<<<<<<<<<<<<<< 4th row >>>>>>>>>>>>>

one = Button(root,text='1',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('1')).grid(row=4,column=0,ipadx =10, ipady=10)
two = Button(root,text='2',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('2')).grid(row=4,column=1,ipadx =10, ipady=10)
three =Button(root,text=' 3 ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('3')).grid(row=4,column=2,ipadx =10, ipady=10)
sub =Button(root,text=' - ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('-')).grid(row=4,column=3,ipadx =10, ipady=10)

#......5th row............

zero =Button(root,text='0',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('0')).grid(row=5,column=0,ipadx =10, ipady=10)
point = Button(root,text='.',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('.')).grid(row=5,column=1,ipadx =10, ipady=10)
equal = Button(root,text=' = ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=Equal).grid(row=5,column=2,ipadx =10, ipady=10)
plus = Button(root,text=' + ',bg='yellow',bd=12,font=('Arial',16,'bold'),command=lambda:press('+'))
plus.grid(row=5,column=3,ipadx =10, ipady=10)

root.mainloop()
