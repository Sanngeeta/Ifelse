num=int(input("enter the Marks"))
if num>80:
    print("A Grade")
    if num<=75:
        print("B Grade")
        if num<=65:
            print("C Grade")
            if num<=60:
                print("D Grade")
                if num<=55:
                    print("E grade")
                    if num<=50:
                        print("G Grade")
                    else:
                        print("marks not difaind") 
                else:          
                    print("marks not difaind")  
            else:
                print("marks not difaind")
        else:
            print("marks not difaind")     
    else:
        print("marks not difaind")
else:
    print("marks not difaind")                    

