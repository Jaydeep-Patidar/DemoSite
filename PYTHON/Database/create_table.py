import mysql.connector
conn=mysql.connector.Connect(
host='localhost',
database='mydatabase',
user='root',
password='root123')

quary='create table student(sid int primary key auto_increment,sname varchar(50),semail varchar(50))'
cur=conn.cursor()
cur.execute(quary)
conn.commit()
print('table create....')
conn.close()







