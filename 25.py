# for i in range(0, 1000):
#     if i%5==0 and i%7==0 and i%13==0:
#         print(i)
def f(n):
    for i in range(2, n):
        if n%i==0:
            return n//i
    return 0
for i in range(224466,664423, 455):
    if i%5**2!=0 and i%7**2!=0 and i%13**2!=0:
        if f(i) < 100000 and str(f(i))[:-2]=='19':
            print(i, f(i))