
#string [start : end+1 :step]
s='python'
print(len(s)) #length of string
print('indexing')
print(s[0]) #0th index
print(s[4]) #4th index
print(s[-2]) #-2nd index
print('slicing')
print(s[0:3]) #start : end-1
print(s[2:4]) #2:4-1=2 to 3
print(s[-6:3]) #-6:-3-1=-6 to 4
print('skip sequence')
print(s[::2])#0,2,4=index of 2
print(s[1::3])#1,4(3-1)=skip 2
print(s[1:4:2]) #1 to 3=skip1(2-1)
