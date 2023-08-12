import mysql.connector
con=mysql.connector.connect(host='localhost',password='root123',user='root')

if con.is_connected():
    print('connection created...')