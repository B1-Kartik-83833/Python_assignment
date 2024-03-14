# 3) Write a Python program to count the elements in a list until an element is a tuple.

def count_elements(my_list):

    count = 0
    for item in my_list:
        if type(item) == tuple:
            break
        count += 1
    return count


my_list = [10, 20, 30, (40,50), 60]
number_of_elements = count_elements(my_list)
print(f"number of elements counted = {number_of_elements}")
