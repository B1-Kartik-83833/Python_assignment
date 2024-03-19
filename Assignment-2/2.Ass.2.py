# 2) Write a program that accepts a list from user and print the alternate element of list.

user_list = []

for i in range(10):
    user_list.append(int(input(f"enter {i+1}th value : ")))

print(user_list[:len(user_list):2])
