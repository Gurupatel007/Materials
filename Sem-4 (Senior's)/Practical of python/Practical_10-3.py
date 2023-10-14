from tkinter import * 
top=Tk() 
top.title('Font') 
top.geometry('500x400') 
font=StringVar() 
def font_change(): 
    f=Lfont.get(ACTIVE) 
    l4.config(font=(f,)) 
def fontSize(): 
    fsize=fontsize.get(ACTIVE) 
    l4.config(font=('',fsize,)) 
def fontStyle(): 
    fsize=fontsize.get(ANCHOR) 
    fstyle=fontstyle.get(ACTIVE) 
    l4.config(font=(' ',fsize,fstyle)) 
l1=Label(top,text='Font',font=('bold',12)) 
l1.place(x=50,y=10) 
l2=Label(top,text='Font Style',font=('bold',12)) 
l2.place(x=190,y=10) 
l3=Label(top,text='Font Size',font=('bold',12)) 
l3.place(x=350,y=10) 
Lfont=Listbox(top) 
Lfont.insert(0,'Times') 
Lfont.insert(1,'Verdana') 
Lfont.insert(2,'Arial') 
Lfont.insert(3,'Courier') 
Lfont.place(x=10,y=40) 

fontstyle=Listbox(top) 
fontstyle.insert(0,'regular') 
fontstyle.insert(1,'italic') 
fontstyle.insert(2,'bold') 
fontstyle.insert(3,'bold italic') 
fontstyle.place(x=165,y=40) 
fontsize=Listbox(top) 
for i in range(0,150): 
   fontsize.insert(i,str(i+1)) 
   fontsize.place(x=320,y=40) 
s=Scrollbar(top,orient='vertical') 
s.place(x=445,y=40,height=165) 
fontsize.config(yscrollcommand=s.set) 
s.config(command=fontsize.yview) 
s.set(0,0) 
l4=Label(top,text='Simple') 
l4.place(x=200,y=300) 
b1=Button(top,text='Font',font=('bold',12),command=font_change) 
b1.place(x=50,y=220) 
b2=Button(top,text='Font =Style',font=('bold',12),command=fontStyle) 
b2.place(x=185,y=220) 
b3=Button(top,text='Font Size',font=('bold',12),command=fontSize)
b3.place(x=345,y=220) 
top.mainloop() 