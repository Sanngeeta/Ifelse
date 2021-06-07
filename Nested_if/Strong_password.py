alpha=input("Enter the charecter:")
number=input("Enter the number:")
nam=input("Enter the specile charecter:")
   
if alpha=="A-Z":
    print("It's alpha")
    if number=="0-9":
        print("It's number")
    elif nam=="@#_&*": 
        print("It's specile charecter")
       
    else:
        print("Invalied")
            
       
else:
    print(alpha+number+nam) 
    print("strong")


