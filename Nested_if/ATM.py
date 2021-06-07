card=input("Insret ATM Card:")
if card=="debitcard" or card=="creditcard":
    print("Please do not Remove you card during Entire Transaction")
    Language=input("Please Select language:")
    if Language=="english":
        print("Proecces")
        pin=input("Enter 4-Digit ATM pin:")
        if pin=="9899":
            print("Your account hasbeen proescces")
            account=input("Select of Transaction:")
            if account=="cash withdrawal":
                print("Inprocess")
                type=input("Please Select your Account:")
                if type=="saving" or type=="current" or type=="depoti":
                    print("Proecces")
                    amount=input("Enter the Amount:")
                    if amount>="10000":
                        print("Collect the Cash")
                        receipt=input("Take a printed receipt , if needed:")
                        if receipt=="yes" or receipt=="no":
                            print("Your Transaction Suesccsfully")
                        else:
                            print("Thnak you")   
                    else:
                        print("can't withdrawal amount more than the balance in your account.") 
                else:
                    print("Account is not difind")  
            else:
                print("Wrong")   
        else:
            print("Your Pin Number incorrect") 
    else:                   
        pin1=input("Apna 4 Aank ka ATM pin number Darj kare:")
        if pin1=="9899":
            print("Apka Khata Pratikiriya kar raha hai")
            type1=input("Apna Transaction Chuiniye:")
            if type1=="saving" or type1=="current" or type1=="deposit":
                amount1=int(input("Apni Rashi Daliye:"))
                if amount1<=10000:
                    print("Apka Khata Pratikriya kar raha hai")
                    print("Apka Cash ekhatha kijiye")
                    receipt1=input("Apko kya rasid chahiye:")
                    if receipt1=="yes" or r1ecepit=="no":
                        print("Apka Transaction safaltapurvak ho gaya hai")
                    else:
                        print("Thank you") 
                else:
                    print("Apne jada Rashi chuni hai, Ek bar me aap sirf 10 hajar tak hi nikal sakte hai")     
            else:
                print("Apka khata Paribhashit nhi ho paa raha hai")             
        else:
            print("Apka pincode number maniye nhi hai")    
else:
    print("Card is not accepted")                    
              


