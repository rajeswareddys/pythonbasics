seq=input('enter the sequence:')
if seq==seq[::-1]:
    print('num {0} is palindrome'.format(seq))
else:
    print('num {0} is not palindrome'.format(seq))