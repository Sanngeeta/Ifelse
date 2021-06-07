
marked=int(input("enter the price"))
if marked>10000:
    print(20/100*marked)
elif marked>7000 and marked<=10000:
    print(15/100*marked)   
elif marked<=7000:
    print(10/100*marked)    
    print("net amount to pay",marked) 
