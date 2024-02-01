f=open('17.txt')
s=[int(x) for x in f.readlines()]
mn103=10**20
for i in range(len(s)):
    if s[i]%103==0:
        mn103=min(mn103, s[i])
mxs=-10**20
k=0
for i in range(len(s)-1):
    if (s[i]+s[i+1])%2==0 and abs(s[i]-s[i+1])%mn103==0:
        k+=1
        mxs=max(mxs, s[i]+s[i+1])
print(k, mxs)