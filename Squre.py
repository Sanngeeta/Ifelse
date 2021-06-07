

a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
d=int(input("enter the fourth side"))
if a==b and c==d:
    print("squre")
elif a==c and b!=d:
    print("rectangle")    
else:
    print("not found")    