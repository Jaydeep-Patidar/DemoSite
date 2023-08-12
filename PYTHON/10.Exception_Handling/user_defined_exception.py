class MyException(Exception):
    pass
c=55
if c>5:
    raise MyException('something went wrong')