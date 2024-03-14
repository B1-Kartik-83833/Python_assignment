# 8) Given a dictionary of students and their favourite colours:
# people={'Aram':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people = {'Aram': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
# A
print(f"students in the list are : {people.keys()}")
# B
people['Lisa'] = 'Black'
# C
people.pop('Jenny')
# D
sorted_keys = sorted(people.keys())
for key in sorted_keys:
    print(key, people[key])









