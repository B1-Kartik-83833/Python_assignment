def Max_in_num():
    num1= int(input("Enter first numbr: "))
    num2 = int(input("Enter Second  numbr: "))
    num3 = int(input("Enter third  numbr: "))

    if (num1>num2 and num1>num3 ):
       print(f"Highet number is {(num1)}")
    elif (num2>num1 and num2>num3 ):
       print(f"Highet number is {(num2)}")
    else: print(f"Highet number is {(num3)}")



Max_in_num()