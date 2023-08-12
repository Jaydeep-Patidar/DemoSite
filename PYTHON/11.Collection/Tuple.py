tup1=(1,2,3,4,5,6)
print(tup1)

tup2=(1,)
print(tup2)

tup3=(1,2,3,4,5,6)
print(tup3)
print('tup3[2]:',tup3[2])
print('tup3[-3]:',tup3[-3])
print('tup3[2:5]:',tup3[2:5])
print('tup3[3:]:',tup3[3:])
print('tup3[:4]:',tup3[:4])
print('tup3*4:',tup3*4)
print('3 in tup3:',3 in tup3)
print('len(tup3):',len(tup3))

tup4=(1,2,3,4,5,6)
for element in tup4:
    print(element)
    
tup5=(1,2,3,4,5,6)
#print(dir(tup5))
#help(tup5.count)

tup6=(1,2,2,4,2,6)
print(tup6.count(2))
print(tup6.index(4))