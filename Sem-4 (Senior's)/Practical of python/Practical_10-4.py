from tkinter import * 
import sqlite3
root = Tk() 
root.geometry('510x510') 
root.title("Registration Form") 
root.config(bg='aqua')

name = StringVar() 
en = StringVar() 
var = IntVar() 
var1 = IntVar() 
Email = StringVar() 
mob = StringVar() 
branch = StringVar() 
add=StringVar()

def database(): 
 name1 = name.get() 
 enr = en.get() 
 gend = var.get() 
 br = branch.get() 
 m = mob.get() 
 e = Email.get() 
 ad=add.get() 
 conn = sqlite3.connect('Form1.db') 
 with conn: 
   cursor = conn.cursor() 
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Enrollment TEXT,Name TEXT,Gender Text,Branch TEXT,Mobile TEXT,Email TEXT,Address TEXT)') 

   cursor.execute('INSERT INTO Student (Enrollment,Name,Gender,Branch,Mobile,Email,Address) VALUES(?,?,?,?,?,?,?)', 
( enr,name1, gend,br,m,e,ad)) 
   conn.commit() 

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20)) 
label_0.place(x=80, y=53) 
label_1 = Label(root, text="Enter Enrolment No:", width=20, font=("bold", 
10)) 
label_1.place(x=68, y=130) 
entry_1 = Entry(root, textvar=en) 
entry_1.place(x=240, y=130) 
label_2 = Label(root, text="Enter Name:", width=20, font=("bold", 10)) 
label_2.place(x=68, y=180) 
entry_2 = Entry(root, textvar=name) 
entry_2.place(x=240, y=180) 
label_3 = Label(root, text="Select Gender", width=20, font=("bold", 10)) 
label_3.place(x=68, y=230) 
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=240, 
y=230) 
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=295, 
y=230) 
label_4 = Label(root, text="Branch", width=20, font=("bold", 10)) 
label_4.place(x=70, y=280) 
op = ['--Select Branch--','Computer Engineering','Information Technology'] 
branch.set(op[0])
w = OptionMenu(root, branch, *op) 
w.place(x = 240,y = 280) 
label_5 = Label(root, text="Mobile", width=20, font=("bold", 10)) 
label_5.place(x=70, y=330) 
entry_2 = Entry(root, textvar=mob) 
entry_2.place(x=240, y=330) 
label_6 = Label(root, text="Email", width=20, font=("bold", 10)) 
label_6.place(x=70, y=380) 
entry_2 = Entry(root, textvar=Email) 
entry_2.place(x=240, y=380) 
label_7 = Label(root, text="Enter Address", width=20, font=("bold", 10)) 
label_7.place(x=70, y=430) 

entry_2 = Entry(root, textvar=add) 
entry_2.place(x=240, y=420,height=50,width=125) 
Button(root, text='Submit',width=20,command=database).place(x=180, y=480) 
root.mainloop()
