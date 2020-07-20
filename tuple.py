# tuple holds items in common brackets
# items in tuple cannot br updated but item in list from tuple can be modified
# tuples also have index values.
# tuples are immmutable

t=([1,2,3,],True,'mahesh')
t[0][1]=4
for i in t:
    print(i,end=' ')
print(' ')
print(t.count(True))#count-number of times element is repeated in tuple
print(t.index('mahesh')) #takeselement values and return index value