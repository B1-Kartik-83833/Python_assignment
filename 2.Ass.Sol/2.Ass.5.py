# 5) Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.

def overlapping():
    list1 = []
    list2 = []

    for i in range(6):
        list1.append(int(input(f"Enter {i+1} elemts to add in the first list .")))
    print("-"*80)
    for j in range(6):
        list2.append(int(input(f"Enter {j+1}elemts to add in the second list .")))

    is_equal = False
    for x in list1:
        for y in list2:
            if (x == y):
                is_equal= True
                break

    if is_equal :
        print("the numebr is overlapping")
    else:
        print("number is not overlapping")




overlapping()
