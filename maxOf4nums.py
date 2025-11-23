a=int(input("enter first number a:"))
b=int(input("enter second number b:"))
c=int(input("enter third number c:"))
d=int(input("enter forth number d:"))
if(a>b):
    if(a>c):
        if(a>d):
            print(a)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d)
else:
    if(b>c):
        if(b>d):
            print(b)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d)