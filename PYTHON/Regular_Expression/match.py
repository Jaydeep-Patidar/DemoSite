'''
import re
pattern='^abc'
mystring='abcd'
print(re.match(pattern,mystring))
'''
import re
pattern=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$)'
email='abc@gmail.com'
print(re.match(pattern,email))
