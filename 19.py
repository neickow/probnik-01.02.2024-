#19
def f(a, p):
    if (a>=100) and (p==3):
        return True
    if (a>=100) and (p==2):
        return False
    if (a<100) and (p==3):
        return False
    if p%2==1:
        return f(a*2,p+1) or f(a*3,p+1)
    if p%2==0:
        return f(a*2,p+1) or f(a*3,p+1)
for s in range(1,99):
    if f(s,1)==True:
        print(s)
        break

