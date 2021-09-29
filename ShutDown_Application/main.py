import os
from tkinter import*


root= Tk()
#root.geometry('250x250')
root.maxsize(width=250,height=250)
root.configure(bg='light green')


def shutdown():
    return os.system("Shutdown /s /t 1")


def restart():
    return os.system("Shutdown /s /t 1")
  
  
  
 
Button(root,text='ShutDown',command=shutdown).place(x=80,y=50)
Button(root,text='Restart',command=restart).place(x=90,y=80)

mainloop()
