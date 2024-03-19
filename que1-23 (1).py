# Write a NumPy program to create an array with the values 1, 7, 13, 105  and determine the size of the memory occupied by the array.
import random

import numpy as np


def function1():
    import sys
    array = np.array([1, 7, 13, 105])
    print(f"size of memory={sys.getsizeof(array[0]) * len(array)}")


# function1()


# Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.


def function2():
    array1 = np.array([1, 2, 4, 5])
    array2 = np.array([5, 2, 7, 5])
    array = array1 > array2
    array_1 = array1 >= array2
    array_2 = array1 < array2
    array_3 = array1 <= array2
    print(array)
    print(array_3)
    print(array_1)
    print(array_2)


# function2()

# Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives, 10 tens, 10 twenty's and 10 fifty's.
def function3():
    onces_10 = np.ones(10)
    print(onces_10)
    zeroes_10 = np.zeros(10)
    print(zeroes_10)
    five_10 = np.ones(10) * 5
    print(five_10)
    tens_10 = np.ones(10) * 10
    print(tens_10)
    twenty_20 = np.ones(10) * 20
    print(twenty_20)
    fifty_50 = np.ones(10) * 50
    print(fifty_50)


# function3()
# Write a NumPy program to create an array of integers from 30 to 70.
def function4():
    array = np.arange(30, 71)
    print(array)


# function4()

# Write a NumPy program to create an array of integers from 50 to 95.
def function5():
    array = np.arange(50, 96)
    print(array)


# function5()
# Write a NumPy program to create an array of all even integers from 20 to 80.
def function6():
    array = np.arange(20, 81)
    print(f"{array[array % 2 == 0]}")


# function6()
# Write a NumPy program to create an array of all odd integers from 20 to 80.
def function7():
    array = np.arange(20, 81)
    print(f"{array[array % 2 != 0]}")


# function7()
# Write a NumPy program to generate an array of 15 random numbers from 10 to 40.
def function8():
    array = np.random.randint(10, 40, 15)
    print(array)


# function8()
# Write a NumPy program to generate an array of 10 random numbers from 30 to 50.
def function9():
    array = np.random.randint(30, 50, 10)
    print(array)


# function9()
# Write a NumPy program to generate an array of 20 random numbers from 50 to 90.
def function10():
    array = np.random.randint(50, 90, 20)
    print(array)


# function10()
# Create any two arrays & perform various mathematical operations.
# i.e. Addition, Substraction, Multiplication, Divide.
def function11():
    array1 = np.array([1, 2, 4, 5])
    array2 = np.array([5, 2, 7, 5])
    array = array1 + array2
    array_1 = array1 - array2
    array_2 = array1 * array2
    array_3 = array1 / array2
    print(array)
    print(array_3)
    print(array_1)
    print(array_2)


# function11()

# Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
def function12():
    array = np.arange(10, 22)
    array2 = array.reshape(3, 4)
    print(array2)


# function12()
#  Write a NumPy program to find the number of rows and columns in a given  matrix
def function13():
    array = np.array([
        [10, 11, 12, 13],
        [14, 15, 16, 17],
        [18, 19, 20, 21]
    ])
    array2 = array.shape
    print(array2)


# function13()
# Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
def function14():
    array = np.random.random((3, 3, 3))
    print(array)


# function14()
#  Write a NumPy program to create a 2x3x4 array filled with arbitrary values
def function15():
    array = np.random.random((2, 3, 4))
    print(array)


# function15()
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
def function16():
    list = [1, 2, 3, 4, 5, 6]
    array = np.array(list)
    print(array)


# function16()
# rite a NumPy program to create a 3x3 matrix with values ranging from  2 to 10.
def function17():
    array = np.arange(10, 22)
    array2 = array.reshape(3, 3)
    print(array2)


# function17()
# Write a NumPy program to create an array with values ranging from 12 to 38.
def function18():
    array = np.arange(12, 38)
    array2 = array.reshape(3, 3)
    print(array2)


# function18()
# Write a NumPy program to reverse an array (the first element becomes the last).
def function19():
    array = np.array([1, 2, 3, 4, 5])
    array2 = array[::-1]
    print(array2)


# function19()
# rite a NumPy program to convert an data type into to a floating type
def function20():
    array = np.array([1, 2, 3, 4], dtype=float)

    print(array)


# function20()
# Write a NumPy program to convert a list array.
def function21():
    list = [1, 2, 3, 4, 5, 6]
    array = np.array(list)
    print(array)


# function21()

# Write a NumPy program to get the element-wise remainder of an array of division.
def function22():
    array = np.remainder([1, 2, 3, 4, 5], 5)
    print(array)


# function22()


# Write a NumPy program to get the element-wise remainder of an array of numbers from 20 to 50 which are divisible by 3.
def function23():
    array = np.arange(20, 51)
    print(f"{array[array % 3 == 0]}")

# function23()
