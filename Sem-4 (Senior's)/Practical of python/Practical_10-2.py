
from tkinter import*
top = Tk()
top.configure(bg="Aqua")
top.geometry("500x500")

def from_kg():
    gram=float(e1.get())*1000
    pounds=float(e1.get())*2.20463
    ounce=float(e1.get())*35.273

    e2.delete("1.0",END)
    e2.insert(END,gram)

    e3.delete("1.0",END)
    e3.insert(END,pounds)

    e4.delete("1.0",END)
    e4.insert(END,ounce)


first =Label(top,text="Enter the wieght in KG")
first.grid(row=0,column=0)
e1=Entry(top)
e1 = Entry(top,textvariable=e1)
e1.grid(row=0,column=1)
convert = Button(top,text="Convert",width=10,command=from_kg)
convert.grid(row=0,column=2,padx=50)
second =Label(top,text="Gram")
second.grid(row=1,column=0)
third = Label(top,text="Pound",width=5)
third.grid(row=1,column=1)
four = Label(top,text="ounce",width=5)
four.grid(row=1,column=2)
e2 =Text(top,height=1,width=20)
e2.grid(row=2,column=0)
e3 =Text(top,height=1,width=20)
e3.grid(row=2,column=1)
e4 =Text(top,height=1,width=20)
e4.grid(row=2,column=2)

top.mainloop()