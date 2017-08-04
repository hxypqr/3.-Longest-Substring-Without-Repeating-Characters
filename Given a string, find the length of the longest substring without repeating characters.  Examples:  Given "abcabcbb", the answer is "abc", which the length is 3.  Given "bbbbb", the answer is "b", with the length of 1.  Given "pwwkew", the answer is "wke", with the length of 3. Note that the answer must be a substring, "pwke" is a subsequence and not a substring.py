a=["a","s","g","h","g","g","r","b","a"]
b=a
print len(a)
print b
k=0
r=0
t=0
l=0
for k in range(0,len(a)):
    for r in range(k+1,len(a)):
        for t in range(k,r-1):
            if a[t]==a[r]:
