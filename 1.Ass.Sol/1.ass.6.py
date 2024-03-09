def eligibilty():
    age=int(input("Enter your age :  "))
    if age>=18:
        print(f"pesron with age {age} is eligible for vote")
    else: print(f"pesron with age {age} is not eligible for vote")
eligibilty()