import mysql.connector
conn=mysql.connector.Connect(host='localhost',database='school',user='root',password='root123')
query="insert into student(sname,semail) values('piyu','pussy@gmail.com')"
cur=conn.cursor()
cur.execute(query)
conn.commit()
print('data inserted...')
conn.close