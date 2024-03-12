#####
# def is_prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# for N in range(41, 1000):
#     s='0'+'1'*40+'2'*N+'0'
#     while '00' not in s:
#         s=s.replace('02', '101', 1)
#         s = s.replace('11' , '2' , 1)
#         s = s.replace('012' , '30' , 1)
#         s = s.replace('010' , '00' , 1)
#     sm=sum(int(x) for x in s)
#     if is_prime(sm):
#         print(N)
#         break
#######
# from ipaddress import *
# ans=0
# ip='171.128.0.0'
# m='255.128.0.0'
# net=ip_network(f'{ip}/{m}', 0)
# for i in net:
#     ipr = (f'{i:b}')[-16:]
#     ipl = (f'{i:b}')[:-16]
#     if ipl.count('1')<ipr.count('1'):
#         ans+=1
# print(ans)
######
# for p in range(5, 10):
#     for x in range(1, p):
#         for y in range(1, p):
#             s1=int('12', p)
#             s2=int('34', p)
#             s3=int(str(x)+str(y)+'2', p)
#             if s1*s2==s3:
#                 print(p, x, y)
#                 print(int('54', 6))
########
# def f(n):
#     if n>1_000_000:
#         return n
#     else:
#         return n+f(2*n)
# def g(n):
#     return f(n)/n
# k=0
# for i in range(1, 1000_001):
#     if g(i)==2047:
#         k+=1
# print(k)
###########
# print('19 ЗАДАНИЕ')
# def f1(a,b, p):
#     if (a>=48 or b>=48) and (p==3): # petya
#         return True
#     if (a>=48 or b>=48) and (p==2): # ivan
#         return False
#     if (a<48 or b<48) and (p==3):  # petro
#         return False
#     if p%2==1:  # petr
#         if a>b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b*2 , p+1)
#         if b>a:
#             return f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1) and f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1)
#     if p%2==0:  # v
#         if a > b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b*2 , p+1)
#         if b > a:
#             return f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1) or f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1)
# mns=10**20
# for s1 in range(1, 51):
#     for s2 in range(1, 51):
#         if f1(s1, s2,1)==True:
#             mns=min(mns, s1+s2)
# print(mns)
#
# print('20 ЗАДАНИЕ')
# def f1(a,b, p):
#     if (a>=48 or b>=48) and (p==4): # petya
#         return True
#     if (a>=48 or b>=48) and (p==3): # ivan
#         return False
#     if (a<48 or b<48) and (p==4):  # petro
#         return False
#     if p%2==0:  # petr
#         if a>b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b*2 , p+1)
#         if b>a:
#             return f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1) and f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1)
#     if p%2==1:  # v
#         if a > b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b*2 , p+1)
#         if b > a:
#             return f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1) or f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1)
# mns=10**20
# for s2 in range(1, 47):
#     if f1(13, s2,1)==True:
#         print(s2)
# print('21 ЗАДАНИЕ')
# def f1(a,b, p):
#     if (a>=48 or b>=48) and (p==3 or p==5): # petya
#         return True
#     if (a>=48 or b>=48) and (p==2 or p==4): # ivan
#         return False
#     if (a<48 or b<48) and (p==5):  # petro
#         return False
#     if p%2==1:  # petr
#         if a>b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b*2 , p+1)
#         if b>a:
#             return f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1) and f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) and f1(a+2 , b , p+1) and f1(a+3 , b , p+1) and f1(a , b+1 , p+1) and f1(a , b+2 , p+1) and f1(a , b+3 , p+1)
#     if p%2==0:  # v
#         if a > b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b*2 , p+1)
#         if b > a:
#             return f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1) or f1(a*2 , b , p+1)
#         if a==b:
#             return f1(a+1 , b , p+1) or f1(a+2 , b , p+1) or f1(a+3 , b , p+1) or f1(a , b+1 , p+1) or f1(a , b+2 , p+1) or f1(a , b+3 , p+1)
# mns=10**20
# for s2 in range(1, 47):
#     if f1(39, s2,1)==True:
#         print(s2)
# print('23 ЗАДАНИЕ')
# def f(a, b):
#     if a==b:
#         return True
#     if a>b:
#         return False
#     if a==11:
#         return False
#     if a==15:
#         return False
#     return f(a+1, b) + f(a*2, b) + f(a+3, b)
# print(f(2, 8)*f(8, 20))
##############
f=open('244.txt')
s=f.readline()
l=0
ans=0
for i in range(len(s)-2):
    if 'A' in s[i:i+3] and 'B' in s[i:i+3] and 'C' in s[i:i+3]:
        l=-2
    else:
        l+=1
        ans=max(ans, l)
print(ans)