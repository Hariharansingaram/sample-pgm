a="123company*/-"
l=[]
b=[]
c=[]
for i in a:
    if i.isalpha():
        l.append(i)
    elif i.isdigit():
        b.append(i)
    else:
        c.append(i)
