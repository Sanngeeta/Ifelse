
user=input("Enter you user ID:")
password=input("Enter your password:")
if user=="sangeeta786":  
    if password=="9899":
        print("login suceccfully Welcome",user)
    else:
        print("Password is invild")       
elif user!="sangeeta786" and password=="9899":
    print("User id is not correct")
elif user=="sangeeta786" and password!="9899":
    print("Your password is worng")
elif user!="sangeeta786" and password!="9899":   
    print("Your user id or password is incorrect Please Create New Account:")
    newuser=input("Enter your new user ID:")
    newpassword=input("Enter your new password:")
    if newpassword>"a" and newpassword<"z" or newpassword>"9" or newpassword=="@#!%$&*/":
        print("Your password is strong")
        print("Your new account hasbeen create successfully")
    else:
        print("Your password is not strong")    









# alpha=input("Enter the charecter:")
# number=input("Enter the number:")
# charecter=input("Enter the specile charecter:")
# if alpha>"a" and alpha<"z":
#     if number<"9":
#         print("its is numerical velu")
#     elif charecter=="@!#$%&*~{}?/":  
#         print("its specile carecter")
#     else:
#         print("it is not specile carecter")    
# else:
#     if alpha+number+charecter:
#         print("its is strong password")










# nam=input("enter of name")
# pas=int(input("enter of passward"))
# if nam=='sangeeta':
#     if pas=='2345':
#         print("its you accout")
#     else:
#         print("wrong the passward")
# elif nam=='preeti':
#     if pas!='2345':
#         print("its not you account") 
# else:

#     print("create your account")


# nam=input("enter the name")
# pas=int(input("enter the passw\ard"))
# if nam=='preeti':
#     if pas=='9876':
#         print("welcom ton new account")
# else:
#     print("thank you")                          
