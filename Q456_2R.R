#4)Write a R program to create a matrix taking a given vector of numbers as input. Display the matrix.
v1=c(1,2,3,4,5,6,7,8,9)
max=matrix(v1,nrow = 3,ncol=3,byrow = T)
print(max)

#5)Write a R program to access the element at 3rd column and 2nd row, only the 3rd row and only the 4th column of a given matrix(c(1:16)) and Give row_names ,col_names.

v2=c(1:16)
print(v2)
v2=matrix(v2,nrow = 4,ncol = 4,byrow = T)
print(v2)
row.names=c("r1","r2","r3","r4")
col.names=c("c1","c2","c3","c4")
martix2.byname=matrix(v2,nrow = 4,ncol = 4,byrow = T,dimnames =list(row.names, col.names) )
print(martix2.byname)
cat("m[2,3]=",martix2.byname['r2','c3'])
cat("m[3,]=",martix2.byname['r3',])
cat("m[,4]=",martix2.byname[,'c4'])


#6)Write a R program to create two 2x3 matrix and add, subtract, multiply and divide the matrixes.
v3=c(1:6)
v4=c(7:12)
print(v3)
matrix.3=matrix(v3,nrow = 2,ncol = 3,byrow = T)
print(matrix.3)
matrix.4=matrix(v4,nrow = 2,ncol = 3,byrow = T)
print(matrix.4)
print(matrix.3+matrix.4)
print(matrix.3-matrix.4)
print(matrix.3*matrix.4)
print(matrix.3/matrix.4)
