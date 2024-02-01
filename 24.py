f=open('24.txt')
s=f.readline()
l=1
mxl=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        l+=1
    else:
        mxl=max(mxl, l)
        l=1
print(mxl)