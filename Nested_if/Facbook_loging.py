user=input("Enter the email address or phone number:")
if user=="sangeeta25jun@gmail.com" or user=="9999777710":
    print("Your user Id is correct")
    password=input("Enter your password:")
    if password=="sangeeta786":
        print("Loging Successfully")
    else:
        print("Password is invalid try again")
    password2=input("Enter your password:")
    if password2=="sangeeta786":
        print("Loging Susccesfully welcome")
    else:
        print("invaid")    
        user1=input("Enter the email address or phone number:")  
elif user1>"a" and  user<"z" or user1<="9":
    print("Your user Id is correct")     
    password2=input("Enter your password:")
    if password2>"a" or password2<"z" or password2<"9":
        print("Create new account successfully")
    else:
                print("Your user password is invalid")   
        # else:
        #     print("Your email address or phone number not correct") 
else:
    print("Your user Id or password is incorrect create new account")                     



        

                

