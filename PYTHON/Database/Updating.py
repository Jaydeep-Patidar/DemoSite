import mysql.connector
conn=mysql.connector.connect(host='localhost',database='school',user='root',password='root123')
query="update student set sname='apple',semail='apple@gmail.com'where sid=2"
cur=conn.cursor()
cur.execute(query)
conn.commit()
print('data updaated...')
conn.close()
