n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
m=sum(l)
if n==m:
    print("perfect")
else:
    print("not")
        

        
