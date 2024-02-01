s=51*7**12 - 7**3 - 22
ans=0
while s>0:
   ans+=s%7
   s=s//7
print(ans)

