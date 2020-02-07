n=input()
m=input()
p=input()
a=[]
b=[]
c=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(len(n)):
    a.append(n[i])
    b.append(m[i])
    c.append(p[i])

l1.append(a[0])
l1.append(b[0])
l1.append(c[0])
l2.append(a[1])
l2.append(b[1])
l2.append(c[1])
l3.append(a[2])
l3.append(b[2])
l3.append(c[2])
l4.append(a[3])
l4.append(b[3])
l4.append(c[3])
x=sorted(l1)
y=sorted(l2)
z=sorted(l3)
zz=sorted(l4)
one=x[0]+y[0]+z[0]+zz[0]
if int(one)>9:
    on=sum(map(int,str(one)))
print(one)
print(on)
