s=input("enter the string:")
ss=input("enter the substring:")
count=0
ns=len(s)
nss=len(ss)
for i in range(0,ns):
    if s[i:i+nss]==ss:
        count=count+1
print(count)        

