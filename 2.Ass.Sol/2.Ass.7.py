# 7) Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.
def filter_long_words():
    list = []
    length = int(input("enter  the length less than 6 : "))
    for i in range(10):
        list.append(input(f"enter {i+1}th string out of 10 =  "))


    print(f"the list is {list}")
    len1 = len(list)
    print(len1)
    new_list = []

    for i in range(length , 10):

        new_list.append(list[i])

    print(f"the new list is{new_list} ")



filter_long_words()

