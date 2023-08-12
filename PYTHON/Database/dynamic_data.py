import mysql.connector
conn=mysql.connector.connect()
def getconnection():
    conn=mysql.connector.connect(host='localhost',database='school',user='root',password='root123')
    return conn;
def insert_student(sname,semail):
    conn=getconnection()
    cur=conn.cursor()
    query="insert into student(sname,semail)values(%s,%s)"
    args=(sname,semail)
    cur.execute(query,args)
    conn.commit()
    conn.close()    
    print('student data insert...')
    
    
def update_student(sname,semail,sid):
    conn=getconnection()
    cur=conn.cursor()
    query="update student set sname=%s,semail=%s where sid=%s"
    args=(sname,semail,sid)
    cur.execute(query,args)
    conn.commit()
    conn.close()    
    print('student data updeted...')
    
    
def delete_student(sid):
    conn=getconnection()
    cur=conn.cursor()
    query="delete from student where sid=%s"
    args=(sid,)
    cur.execute(query,args)
    conn.commit()
    conn.close()    
    print('student data deleted...')
    
    
def select_all_student():
    conn=getconnection()
    cur=conn.cursor()
    query="select * from student"
    cur.execute(query)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows