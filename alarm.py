# import tkinter
# from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.messagebox import*
# import datetime
# from playsound import playsound
# root=TK()
# def alarm():
#     if x.get()=="AM":
#         h=int(c.get())
#         m=int(c1.get())
#     if x.get()=="PM":
#         h=int(c.get())
#         m=int(c.get())
#     show("alarm notication","alarm has been set")
#     while True:
#         if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
#             j=1
#             while j<=2:
#                 playsound("https://musikringtone.com//downloads//3394//")
#                 show("your alarm is ringing get up")
#                 j=j+1
# root.mainloop()


            

from tkinter import*
from tkinter.ttk import Combobox
from tkinter.messagebox import*
import datetime
from playsound import playsound

root=Tk()

def alarm():
    h=int(c.get())
    m=int(c1.get())
    
    showinfo("alarm notication","alarm has been set")
    print(datetime.datetime.now())
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
            for j in range(2):
                playsound('https://musikringtone.com//downloads//5380//')
                break
root.title(" my alaram clock")

l1=Label(root,text="set alarm hour")
l1.grid(row=0,column=0)
hour=list(range(1,25))
c=Combobox(root,values=hour)
c.grid(row=0,column=1)
 

l2=Label(root,text="set alarm minute")
l2.grid(row=1,column=0)
minute=list(range(0,61))
c1=Combobox(root,values=minute)
c1.grid(row=1,column=1 )


btn=Button(root,bg="red",fg="black",text="set alarm",command=alarm)
btn.grid(row=2,column=2)
root.mainloop()