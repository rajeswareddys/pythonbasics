#consider two variables a,b
#result stored into result variable
a=input('enter the a value:')
b=input('enter the b value:')
result=a+b #concatenation operation will be bcoz it accept as string not as int
result=int(a)+int(b) #explicitly convert string as int by using type conversion
print(type(result),' ',result)
result=int(a)-int(b)
print(type(result),' ',result)
result=int(a)*int(b)
print(type(result),' ',result)
result=int(a)/int(b)  # division will return float value
print(type(result),' ',result)
result=int(a)//int(b)   # division will return int value
print(type(result),' ',result)
result=int(a)**int(b)
print(type(result),' ',result)
result=int(a)%int(b)
print(type(result),' ',result)