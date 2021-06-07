
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b>c:
    print(a,b,"greater number")
elif c>b>a:
    print(c,b,"greater number")
elif b>c>a:
    print(b,c,"greater number")
elif a>c>b:
    print(a,c,"greter number")
elif c>a>b:
    print(c,a,"greater number")
elif b>a>c:
    print(b,a,"greatre number")
elif c>a>b:
    print(c,a,"grater number")
elif b>a>c:
    print(b,a,"greter number")
else:
    print("All number are equal")    




a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
if a>b and c>d:
    print(a,"greater tha",b and c,"gerater than",d)
else:
    print("both are not greater than")    
