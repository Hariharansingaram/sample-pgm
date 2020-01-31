num=int(input())
a=input()
b=input()
l=[]
for i in range(0,num):
    d=input()
    if d == a:
        l.append(b)
    else:
        l.append(d)
print(l)
e='-'.join(l)
print(e)
        
