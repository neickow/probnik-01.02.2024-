def f(a, p):
    if (a>=100) and (p==4):
        return True
    if (a>=100) and (p==3):
        return False
    if (a<100) and (p==4):
        return False
    if p%2==0: # vanya
        return f(a*2,p+1) and f(a*3,p+1)
    if p%2==1: # petro
        return f(a*2,p+1) or f(a*3,p+1)
for s in range(1,99):
    if f(s,1)==True:
         print(s)