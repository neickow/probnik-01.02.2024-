import itertools
alp=itertools.product('ЩОГБА', repeat=6)
k=0
for i in alp:
    s=''.join(i)
    k+=1
    if s=='ОБЩАГА':
        print(k)
