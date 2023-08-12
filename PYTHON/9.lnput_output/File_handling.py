path='C:\\Users\\jaydeep patidar\\Desktop\\baba.txt'
file=open(path,'r')
#content=file.read()
#print(content)

for content in file.read():
    print(content,end='')

#content=file.read(10)
#print(content,end='')
#content=file.read(10)
#print(content,end='')

'''
file=open('text.txt','w')
content='these is the file'
file.write(content)
print('data successfully written')
'''
'''
file=open('text.txt','a')
content='hello these is a file'
file.write(content)
print('data successfully written')
'''
'''
path='C:\\Users\\jaydeep patidar\\Desktop\\baba.txt'
file=open(path,'r')
content=file.read()
print(content)
print(file.tell())
file.seek(2,0)
content=file.read()
print(content)
'''