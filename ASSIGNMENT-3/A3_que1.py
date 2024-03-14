def function():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    new_list = []
    for i in list1:
        for j in list2:
            word=i+j
            new_list.append(word)
    print(new_list)


function()
