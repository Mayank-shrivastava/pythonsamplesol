l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i==0:
        a.append(i)
    else:
        b.append(i)
b.extend(a)
print(b)
