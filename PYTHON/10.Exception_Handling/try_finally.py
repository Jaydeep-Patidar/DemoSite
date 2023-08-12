print('hello')
try:
    c=int(input('enter value'))+4
    c=b+4
except ValueError:
    print('error! you can not enter string')
except NameError:
    print('error! variable not define')
except Exception:
    print('error! some thing went wrong')
finally:
    print('in finallly')
print('good bye')