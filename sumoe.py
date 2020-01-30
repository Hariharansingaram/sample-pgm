a=int(input())
l=[]
for i in range(0,a):
    l.append(int(input()))
a=l[0::2]
b=l[1::2]
print(sum(a))
print(sum(b))
    
