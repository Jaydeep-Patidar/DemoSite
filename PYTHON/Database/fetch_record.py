import mysql.connector
conn=mysql.connector.Connect(host='localhost',database='school',user='root',password='root123')
query="select*from student"
cur=conn.cursor()
cur.execute(query)
rows=cur.fetchall()
conn.commit()
#print(rows)
for row in rows:
    #print(row)
    print('student roll no:',row[0])
    print('student name:',row[1])
    print('student email:',row[2])
    print()
conn.close