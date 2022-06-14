from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime
from playsound import playsound

root=Tk()

def alarm():
    if x.get()=="AM":
        h=int(c.get())
        m=int(c1.get())

    if x.get()=="PM":
        h=int(c.get())+12
        m=int(c1.get())
    
    showinfo("alarm notication","alarm has been set")
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
                playsound("https://musikringtone.com//downloads//3394//")
                showinfo("alarm notificarion","wake upke")
            
root.title(" my alaram clock")

l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(0,13))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)
 
            
