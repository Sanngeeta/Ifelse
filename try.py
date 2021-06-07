a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if b>a and b>c or c<a:
    print(a,"maxsium")
elif b>c and c<a or a>b:
    print(b,"maxisum")
elif c<a and a>b or b>c:
    print(c,"maxium") 
else:
    print(b,"maxium")       

