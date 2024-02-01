f=open('27A.txt')
s=f.readlines()
f.close()
N=int(s.pop(0))
s=[int(x) for x in s]
k=0
for i in range(N-1):
    for g in range(i):
        if (s[i] + s[g]) % 131 == 0:
            k += 1
print(k)