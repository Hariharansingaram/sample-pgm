                                                                                                                                                                                          
inp1='Raagam'
inp2='Talam'
inp3='Pallavi'
l1=len(inp1)
l2=len(inp2)
l3=len(inp3)
if l1%3==1:
    f1=inp1[:l1-3]
    up1=f1.capitalize()
    f2=inp1[l1-3:l1-1]
    f3=inp1[l1-1:]
elif l1%3==0:
    if l1//3==2:
        g1=inp1[:l1-3]
        up1=g1.capitalize()
        g2=inp1[l1-3:l1]
    elif l1//3==3:
        g1=inp1[:l1-6]
        up1=g1.capitalize()
        g2=inp1[l1-6:l1-3]
        g3=inp1[l1-3:]
        
else :
    h1=inp1[:l2-3]
    h2=inp1[l2-3]
    h3=inp1[l2-2:]
if l2%3==1:
    i1=inp2[:l1-3]
    i2=inp2[l1-3:l1-1]
    i3=inp2[l1-1:]
elif l2%3==0:
    if l2//3==2:
        j1=inp2[:l2-3]
        up2=j1.capitalize()
        j2=inp2[l2-3:l2]
    elif l2//3==3:
        j1=inp2[:l2-6]
        up2=j1.capitalize()
        j2=inp2[l2-6:l2-3]
        j3=inp2[l2-3:]
else :
    k1=inp2[:l2-3]
    up2=k1.capitalize()
    k2=inp2[l2-3]
    k3=inp2[l2-2:]
if l3%3==1:
    m1=inp3[:l1-3]
    m2=inp3[l1-3:l1-1]
    m3=inp3[l1-1:]
elif l3%3==0:
    if l3//3==2:
        n1=inp3[:l3-3]
        up3=n1.capitalize()
        n2=inp3[l3-3:l3]
    elif l3//3==3:
        n1=inp3[:l3-6]
        up3=n1.capitalize()
        n2=inp3[l3-6:l3-3]
        n3=inp3[l3-3:]
else :
    o1=inp3[:l2-3]
    o2=inp3[l2-3]
    o3=inp3[l2-2:]
op1=up1+k2+m3
op2=f2+k3+up3
op3=f3+up2+n2
op4=op3.swapcase()
print(op1)
print(op2)
print(op4)

    
