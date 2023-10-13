from tkinter import *
top=Tk()
top.geometry('300x200')
t=Entry(top)
t.pack()
def Display():
    msg.config(text=t.get(),width=300)
b=Button(top,text="Click",command=Display)
b.pack()
msg=Message(top)
msg.pack()
top.mainloop()
