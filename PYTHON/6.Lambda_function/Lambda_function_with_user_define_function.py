def g(number):
    return lambda n: number**n
x=g(6)
print(x(3))
print(x(5))