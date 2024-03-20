#Q1 create a data frame for Students information
# columns: RollNo, StudentsName, Age, Score

# get number of columns
# get number of rows
# get columns
# get first 3 rows
# get last 3 rows
# get general information
# get statistical information

name = c("Kartik","Hritik","Akshay","Tushar","Kunal","Pranav")
rollno = c(12,34,23,32,16,65)
age = c(22,23,23,24,22,23)
score = c(98,100,96,35,66,97)

df = data.frame(name,rollno,age,score)
print(df)

print(head(df,3))
print(ncol(df))
print(nrow(df))
print(colnames(df))
print(tail(3))
print(str(df))
print(summary(df))