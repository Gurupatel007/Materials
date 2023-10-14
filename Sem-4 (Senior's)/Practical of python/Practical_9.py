from sqlite3 import Cursor
import pymysql

con = pymysql.connect(host="localhost",user="root",passwd="tiger",database="demo")
# if con:
#     print("Connection successfully")
# else:
#     print("Conncetion lost")

print("")

query = "create table hospital_details(hospital_id int,name varchar(20),bed_count int);"
query1="insert into hospital_details values(1,'Janta',200);"
query2="insert into hospital_details values(2,'Zydus',500);"


try:
    Cursor = con.cursor()
    Cursor.execute(query2)

except pymysql.DatabaseError as e:
    print("wrong",e)
con.commit()



