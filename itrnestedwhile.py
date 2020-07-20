l=[[1,2,3],[4,5,6],[7,8,9]]
len_q=len(l)
ref=0
i=0
while ref<len_q:
    i=l[ref]
    ref_sub=0
    while ref_sub < len(i):
       print(i[ref_sub],end=' ')
       ref_sub+=1
    ref+=1