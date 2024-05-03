import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="school")
mycursor=mydb.cursor()
rno=int(input("enter student number:"))
name=input("enter student name:")
age=int(input("enter student age"))
address=input("enter student address")
sql="INSERT INTO student1(rno,name,age,address) VALUES (%s,%s,%s,%s)"
val=(rno,name,age,address)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")