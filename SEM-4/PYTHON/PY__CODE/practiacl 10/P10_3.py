from tkinter import *
top=Tk()
top.geometry("500x500")
font=StringVar()

def Font_change():
    f=lfont.get(ACTIVE)
    l4.config(font=(f,))

def font_style():
    fsize=fontsize.get(ACTIVE)
    fstyle=fontstyle.get(ACTIVE)
    l4.config(font=('',fsize,fstyle))

def Font_size():
    fsize=fontsize.get(ACTIVE)
    l4.config(font=('',fsize,))

l1=Label(top,text="FontName")
l1.grid(row=0,column=0)

l2=Label(top,text="FontStyle")
l2.grid(row=0,column=1)

l3=Label(top,text="FontSize")
l3.grid(row=0,column=2)

lfont=Listbox(top)
lfont.insert(0,"Times")
lfont.insert(1,"Helvetica")
lfont.insert(2,"Arial")
lfont.insert(3,"Courier")
lfont.grid(row=1,column=0)

fontstyle=Listbox(top)
fontstyle.insert(0,'Regular')
fontstyle.insert(1,'italic')
fontstyle.insert(2,'bold')
fontstyle.insert(3,'bold italic')
fontstyle.grid(row=1,column=1)

fontsize=Listbox(top)
for i in range(150):
    fontsize.insert(i,str(i+1))
    fontsize.grid(row=1,column=2)
s=Scrollbar(top,orient="vertical")
s.grid(row=1,column=3)
fontsize.config(yscrollcommand=s.set)
s.config(command=fontsize.yview)
s.set(0,0)

l4=Label(top,text="Sample")
l4.grid(row=3,column=1)

b1=Button(top,text='Font',command=Font_change)
b1.grid(row=2,column=0)

b2=Button(top,text='Font',command=font_style)
b2.grid(row=2,column=1)

b3=Button(top,text='Font',command=Font_size)
b3.grid(row=2,column=2)

top.mainloop()
