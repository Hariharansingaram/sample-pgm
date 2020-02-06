n=int(input())
a=n**2
b=str(a)
c=len(b)//2
d=int(b[:c]) + int(b[c:])
if n==d:
    print("kaprekar number")
else:
    print("not")  
