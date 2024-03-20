
#Q2 Create a data frame for Students information
#columns: RollNo, StudentsName, Age, Score
#Write a R program to extract 3rd and 5th rows with 1st and 3rd columns from a given data frame.

rollno = c(12,34,23,32,16,65)
name = c("Kartik","Hritik","Akshay","Tushar","Kunal","Pranav")
age = c(22,23,23,24,22,23)
score = c(98,100,96,35,66,97)

df = data.frame(rollno,name,age,score)
print(df)

print(df[3,1])
print(df[5,1])
print(df[3,3])
print(df[5,3])