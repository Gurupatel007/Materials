import pymysql
from tkinter import *
from tkinter import ttk

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="12345",
  database="guru"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student_info (enrollment_no VARCHAR(11), name VARCHAR(255), gender VARCHAR(6), address VARCHAR(255), branch VARCHAR(5), mobile VARCHAR(10), email VARCHAR(255))")

def submit():
    enrollment_no = enrollment_no_entry.get()
    name = name_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", "end-1c")
    branch = branch_combobox.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    mycursor.execute("INSERT INTO student_info (enrollment_no, name, gender, address, branch, mobile, email) VALUES (%s, %s, %s, %s, %s, %s, %s)", (enrollment_no, name, gender, address, branch, mobile, email))
    mydb.commit()

    enrollment_no_entry.delete(0, END)
    name_entry.delete(0, END)
    male_radio.deselect()
    female_radio.deselect()
    address_text.delete("1.0", END)
    branch_combobox.set("")
    mobile_entry.delete(0, END)
    email_entry.delete(0, END)

def view():
    mycursor.execute("SELECT * FROM student_info")
    rows = mycursor.fetchall()

    view_window = Tk()
    view_window.title("View Data")

    tree = ttk.Treeview(view_window)
    tree["columns"] = ("enrollment_no", "name", "gender", "address", "branch", "mobile", "email")
    tree.column("#0", width=0, stretch=NO)
    tree.column("enrollment_no", width=100)
    tree.column("name", width=100)
    tree.column("gender", width=100)
    tree.column("address", width=200)
    tree.column("branch", width=100)
    tree.column("mobile", width=100)
    tree.column("email", width=200)

    tree.heading("enrollment_no", text="Enrollment No.")
    tree.heading("name", text="Name")
    tree.heading("gender", text="Gender")
    tree.heading("address", text="Address")
    tree.heading("branch", text="Branch")
    tree.heading("mobile", text="Mobile No.")
    tree.heading("email", text="Email")

    for row in rows:
        tree.insert("", END, text="", values=row)
    tree.pack()

root = Tk()
root.title("Registration Page")

enrollment_no_label = Label(root, text="Enter Enrollment No.:")
enrollment_no_label.grid(row=0, column=0, padx=10, pady=10)
enrollment_no_entry = Entry(root, width=30)
enrollment_no_entry.grid(row=0, column=1)

name_label = Label(root, text="Enter Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = Entry(root, width=30)
name_entry.grid(row=1, column=1)

gender_label = Label(root, text="Select Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=10)
gender_var = StringVar()
male_radio = Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=2, column=1)
female_radio = Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=2, column=2)

address_label = Label(root, text="Enter Address:")
address_label.grid(row=3, column=0, padx=10, pady=10)
address_text = Text(root, height=5, width=30)
address_text.grid(row=3, column=1)

branch_label = Label(root, text="Select Branch:")
branch_label.grid(row=4, column=0, padx=10, pady=10)
branch_combobox = ttk.Combobox(root, width=27, state="readonly")
branch_combobox["values"] = ("CE", "IT", "AI", "CSBS")
branch_combobox.grid(row=4, column=1)

mobile_label = Label(root, text="Enter Mobile No.:")
mobile_label.grid(row=5, column=0, padx=10, pady=10)
mobile_entry = Entry(root, width=30)
mobile_entry.grid(row=5, column=1)

email_label = Label(root, text="Enter Email:")
email_label.grid(row=6, column=0, padx=10, pady=10)
email_entry = Entry(root, width=30)
email_entry.grid(row=6, column=1)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=7, column=0, padx=10, pady=10)
view_button = Button(root, text="View", command=view)
view_button.grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
