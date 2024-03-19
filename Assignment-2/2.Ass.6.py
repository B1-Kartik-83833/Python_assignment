# 6) Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard.

def find_max(mylist):
    max_element = mylist[0]
    for i in mylist:
        if i > max_element:
            max_element = i
    return max_element

mylist = []
for j in range(5):
    num = int(input(f"Enter {j+1}th number : "))
    mylist.append(num)

result = find_max(mylist)
print(f"The maximum element is {result}")
