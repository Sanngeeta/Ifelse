num1=int(input("enter the first side"))
num2=int(input("enter the second side"))
num3=int(input("enter the third side"))
if num1+num2>num3 and num2+num3>num1 and num1+num3>num2:
    print("triangle is possible")
else:
    print("trianfle not possible")


num1=int(input("enter the first side"))
num2=int(input("enter the second side"))
num3=int(input("enter the third side"))
if num1+num2==80:
    print("triangle is possible")
else:
    print("triangle not possible")    


num1=int(input("enter the first side"))
num2=int(input("enter the second side"))
num3=int(input("enter the third side"))
if num1%num2==0 and num2%num3==0 and num3%num1==0:
    print("triangle is possible")
else:
    print("triangle not possible")


num1=int(input("enter the number"))
if num1%5==0 and num1%10:
    print("it's triangle")
else:
    print("triangle not possible")

na=(input("enter the alph"))
ny="OUEAouea"
if na in ny:
    print("it's triangle")
else:
    print("triangle not possible")        