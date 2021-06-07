
working=int(input("enter the total working days"))
absent=int(input("enter the days of absent"))
days=(working-absent)/working*100
print("Your attendance is ",days)
if days>75:
    print("student eligible for exam")
else:
    print("student not eligible for exam")    
