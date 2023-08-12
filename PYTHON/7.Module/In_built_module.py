import random
import math
import user_define_module 
import user_define_module as jay

#======random module==============#
n=random.randint(1000,9999)
print(n)
#======math module================#
print(dir(math))

help(math.ceil)

x=55.42
print(math.ceil(x))
print(math.floor(x))
print(math.pow(5,3))
print(math.sqrt(16))

print(math.pi)

fact=math.factorial(5)
print(fact)

#=====user define module==========#
user_define_module.getdata(3,"Patidar")
user_define_module.sum(8,3)
#======as=========================#
jay.getdata(2,"jaydeep")
jay.sum(2, 6)