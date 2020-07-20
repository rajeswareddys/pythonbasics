a=5
b=0
try:
    print(a/b)
except Exception as e:
    print(e)
    print('divide by error')
finally:
    print('always execute')