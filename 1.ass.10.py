def Grade():
    sub1 = int(input("Enter marks of sub1: "))
    sub2 = int(input("Enter marks of sub2: "))
    sub3 = int(input("Enter marks of sub3: "))
    Total_marks_obtained = sub1 + sub2 + sub3
    avg = (Total_marks_obtained // 3)
    if avg > 90:
       print('Grade is Excellent')
    elif (avg >= 80 and avg < 90):
        print('Grade is A')
    elif (avg >= 70 and avg < 80):
        print('Grade is B')
    elif (avg>= 60 and avg < 70):
        print('Grade is C')
    elif avg< 60:
         print('Grade is Fail')


Grade()
