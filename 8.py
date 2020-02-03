a=input().split()
b=input().split()
for i in a:
    if i[0] not in b:
        print(i)
