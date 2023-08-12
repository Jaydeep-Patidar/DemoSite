import mysql.connector
conn=mysql.connector.connect(host='localhost',database='school',user='root',password='root123')
query="delete from student where sid=1"
cur=conn.cursor()
cur.execute(query)
conn.commit()
print('data deleted...')
conn.close()
