import cgi, cgitb 
import mysql.connector
print("Content-type:text/html\r\n\r\n")

print("<html>") 
print("<head>")
print("<title>Signup</title>")
print("</head>") 
print("<body>")
print("<form action='Signup.py' method='post'>") 
print("Enter Email: <input type ='text' name = 'email'> <br><br>") 
print("Enter Username: <input type='text' name='un'> <br><br>") 
print("Enter Password: <input type='password' name='pw'> <br><br>")
print("<input type='submit' value='Sign Up'>") 
print("<ahref='Signin.py'>SignIn</a>")
form = cgi.FieldStorage()
email = form.getvalue('email') 
username= form.getvalue('un')
password = form.getvalue('pw')
conn =mysql.connector.connect(host="localhost",user='root',passwd="",database="karan" )
cursor = conn.cursor();
sql="""insert into signup1(email,username,password) 
values(%s,%s,%s)""" 
val=(email,username,password)
cursor.execute(sql,val)
conn.commit()
print("<h2>%s record inserted</h2>" % (cursor.rowcount))
print('</body>')
print('</html>')
