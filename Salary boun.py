
period=int(input("enter the time period of service"))
salary=int(input("enter the salary"))
if period<10:
    print(10/100*salary)
if period>=6 and period<=10:
    print(8/100*salary)  
if period<=6:
    print(5/100*salary)
else:
    ("no boun")    