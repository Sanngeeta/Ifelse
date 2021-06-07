

age1=int(input("enter the first age"))
age2=int(input("enter the second age"))
age3=int(input("enter the third age"))
age4=int(input("enter the fourth age"))
if age1<age2 and age1<age3 and age1<age4:
    print("age of youngest persion is ",age1)
if age2<age1 and age2<age3 and age2<age4:
    print("age of youngest persion is",age2)   
if age2<age1 and age3<age2 and age3<age4:
    print("age of youngest persion is",age3)
if age4<age1 and age4<age2 and age4<age3:
    print("age of youngest persion is",age4)     
else:
     print("age is not difind")     
