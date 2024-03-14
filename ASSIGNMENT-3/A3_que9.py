def sum_of_keys():
    dict1 = {"key": 200, "key2": 300}
    list_1 = []
    for key in dict1:
        print(f"Appended list:{list_1.append(dict1[key])}")
    print(list_1)
    print(sum(list_1))


sum_of_keys()
