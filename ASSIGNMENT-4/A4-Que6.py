# 6) Write a Python program to double all numbers in a given list of integers. Use Python map,lambda function.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda n: n * 2
double = list(map(func, numbers))
print(double)
