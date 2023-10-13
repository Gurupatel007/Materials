from tkinter import *
def selection():
    mystring="You have selected option:"+str(radio.get())
    lb2.config(text=mystring)

top=Tk()
top.geometry('300x200')
radio=IntVar()
lb1=Label(top,text="My Favourite Programming Language:").pack(anchor=N)
r1=Radiobutton(top,text='C++',variable=radio,value=1,command=selection).pack(anchor=W)
r2=Radiobutton(top,text='Java',variable=radio,value=2,command=selection).pack(anchor=W)
r3=Radiobutton(top,text='Python',variable=radio,value=3,command=selection).pack(anchor=W)
lb2=Label(top)
lb2.pack()
top.mainloop()