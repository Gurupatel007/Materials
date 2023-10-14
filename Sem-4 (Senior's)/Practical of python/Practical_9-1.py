import sqlite3 
con=sqlite3.connect("demo_data") 
 
f=open('P9.sql','r') 
query=f.read() 
try: 
        cursor=con.cursor()         
        cursor.executescript(query)         
        con.commit()         
        print("hospital_details tabel is Created in Database demo")         
        print("doctor_details tabel is Created in Database demo")         
        print("hospital_details Record Inserted")         
        print("doctor_details Record Inserted") 
except Exception as ex: 
        print(ex) 
finally: 
        f.close()         
if cursor: 
            cursor.close()         
if con: 
            con.close() 
