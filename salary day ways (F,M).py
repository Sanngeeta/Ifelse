age=int(input("Enter your age"))
sex=input("Enter sex(M/F) ")
yn = int(input("Enter number of days"))
atm=0
if age>=18 and age<30 and sex.upper()=="M":
    atm=yn*700
    print("Total day is",atm)
elif age>=18 and age<30 and sex.upper()=="F":
    atm=yn*750
    print("total day is",atm)   
elif age>=30 and age<=40 and sex.upper()=="M":
    atm=yn*800
    print("tatal day is",atm)
elif age>=30 and age<=40 and sex.upper=="F":
    atm=yn*850
    print("total day is",atm)   
else:
    print("ege is not difind")         

