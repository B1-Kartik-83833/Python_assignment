num1 = int(input("enter the numbers1="))
num2 = int(input("enter the numbers2="))
num3 = int(input("enter the numbers3="))
num4 = int(input("enter the numbers4="))
num5 = int(input("enter the numbers5="))
num6 = int(input("enter the numbers6="))


def repetetion():
    list=[]
    list.append(num1)
    list.append(num2)
    list.append(num3)
    list.append(num4)
    list.append(num5)
    list.append(num6)
    print(f"list form :{list}")
    new_tuple = tuple(list)
    print(f"new tuple form:{new_tuple}")
    new_set = set(new_tuple)
    print(f"new set form:{new_set}")
    repeted_tuple_ele = tuple(new_set)
    print(f"Repeted_tuple_ele={repeted_tuple_ele=}")


repetetion()
