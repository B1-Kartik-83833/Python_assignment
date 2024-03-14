def number_type_check():
    mylist = [41, 'DROND', 'Sunbeam', 13, 'ARA']

    for i in range(0,len(mylist)):
        if type(mylist[i]) == type(0):
            print(f"{mylist[i]},{mylist[i]},{mylist[i]}")
        elif type(mylist[i]) != type(0):
            print(f"#")
        else:
            print(f"invalid list")


number_type_check()
