'''import os
path='c:\\users\\jaydeep patidar\\desktop'
print(os.listdir(path))
#os.rename('c:\\users\\jaydeep patidar\\desktop\\baba.txt','c:\\users\\jaydeep patidar\\desktop\\babaji.txt')
#or
old='c:\\users\\jaydeep patidar\\desktop\\babaji.txt'
new='c:\\users\\jaydeep patidar\\desktop\\baba.txt'
os.renames(old, new)
print(os.listdir(path))
'''

''''
import os
path='c:\\users\\jaydeep patidar\\desktop'
print(os.listdir(path))
old='c:\\users\\jaydeep patidar\\desktop\\baba.txt'
new='c:\\users\\jaydeep patidar\\desktop\\newdir\\baba.txt'
os.renames(old, new)
print(os.listdir(path))
'''
'''
import os
print(os.getcwd())
'''

import os
path='c:\\users\\jaydeep patidar\\desktop\\newdir\\baba.txt'
os.remove(path)