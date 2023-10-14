from ctypes.wintypes import HANDLE
from tkinter import*
top= Tk()
top.geometry("400x200")
top.title("Calculator")
def sum(op):
    n1=int(e1.get())
    n2=int(e2.get())
    if(op=='+'):
        ans=n1+n2
    elif(op=='-'):
        ans=n1-n2
    elif(op=='*'):
        ans=n1*n2
    elif(op=='/'):
        ans=n1/n2
    ans = "Answer is:"+str(ans)
    l1.config(text=ans)
    


first = Label(top,text="Enter Number1:").grid(row=0,column=0)
e1 = Entry(top)
e1.grid(row=0,column=1,columnspan=2)
second = Label(top,text="Enter Number2:").grid(row=1,column=0)
e2 = Entry(top)
e2.grid(row=1,column=1,columnspan=2)
first_button = Button(top,text="+",cursor="circle",foreground="Black",background="red",width=5,command=lambda:sum('+')).grid(row=2,column=1,pady=5)
second_button = Button(top,text="-",foreground="Black",background="red",width=5,command=lambda:sum('-')).grid(row=2,column=2,pady=5)
third_button = Button(top,text="*",foreground="Black",background="red",width=5,command=lambda:sum('*')).grid(row=4,column=1,pady=5)
four_button = Button(top,text="/",foreground="Black",background="red",width=5, command=lambda:sum('/')).grid(row=4,column=2,pady=5)
l1= Label(top)
l1.grid(row=5,column=1,columnspan=2)



top.mainloop()