import math

C= 50
H = 30
Ds = []
result =[]
Dv=input("enter the value of D\n")
Ds=Dv.split(",")
Ds = [int(i) for i in Ds]
i=0
l = len(Ds)
while(i<l):
    Q = round(math.sqrt((2*C*Ds[i])/H))
    result. append(Q)
    i+=1
print("output=",result)

   
    
    
    
    
