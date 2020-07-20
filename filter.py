def even_check(num):
    if num%2==0:
        return True
lis=range(0,21)
print(list(filter(even_check,lis)))