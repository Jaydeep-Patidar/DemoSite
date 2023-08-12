m=lambda:print('welcome to lambda function')
m()

m= lambda a,b:print('sum=',a+b)
m(25,15)

def evalute(a,b,c):
    return lambda x:a*x**2+b*x+c
ans=evalute(3,4,2)
print(ans(4))

