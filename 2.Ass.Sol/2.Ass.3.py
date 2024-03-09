#) Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].

list = ['a','b','c','d','e']
index = list.index('b')
list.pop(index)
for i in range(1, 4):
    list.insert(index, i)
    index += 1

print(list)
