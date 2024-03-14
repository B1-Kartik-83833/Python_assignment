# 7) Write a Python program to convert a given list of integers and a tuple of integers into a list  of strings.Use
# Python map.


numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (6, 7, 8, 9, 10)

string_list1 = list(map(lambda n: str(n), numbers_list))
string_list2 = list(map(lambda n: str(n), numbers_tuple))

print(string_list1)
print(string_list2)










