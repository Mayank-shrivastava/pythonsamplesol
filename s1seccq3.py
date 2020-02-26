l=list(map(int,input().split()))
temp=[i for i in range(1,(max(l)+1))]
ans=[]
for i in temp:
    if i not in l:
        ans.append(i)
print(ans)        
    
    






    


