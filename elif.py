name=input('enter the appilcant:')
age=input('enter ur age:')
income=input('enter ur income per annum')
if int(age)>=18 and int(income)<=10000:
        print(name+' your are eligible to apply ration card')
elif int(age)<=18 and int(income)<=10000:
        print(name+' you are not eligible bcoz income more than poverty line')
else:
    print('not eligible')