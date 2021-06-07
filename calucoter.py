num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
symbol=input("enter the opertor")
(input("enter the operator number"))
if symbol=="+":
    print(num1+num2)
elif symbol=="-":
    print(num1-num2)
elif symbol=="/":
    print(num1/num2)        
elif symbol=="*":
    print(num1*num2) 
elif symbol=="**":
    print(num1**num2)       
elif symbol=="%":
    print(num1%num2)
elif symbol=="//":
    print(num1//num2)
else:
    print("error")     


num=int(input("enter the days"))
if num<=100:
    atm=0
elif num>200 and num<=300:
    atm=num-100*2
elif num>300:
    atm=num+num-300*5
    print("total payment to pay",atm)           



