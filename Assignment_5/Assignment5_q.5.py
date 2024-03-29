import math


class Circle:
    def __init__(self, a, b, r):
        self.__a = a
        self.__b = b
        self.__r = r

    def print_info(self, a, b, r):
        print(f"a:{self.__a}")
        print(f"b:{self.__b}")
        print(f"r:{self.__r}")

    def area_circle(self, a, b, r):
        radia = math.sqrt((a - 0) ** 2 + (b - r) ** 2)
        area = 2 * 3.14 * radia * radia
        print(f"area={area}")

    def perimeter(self, a, b, r):
        radia = math.sqrt((a - 0) ** 2 + (b - r) ** 2)
        perimeter = 2 * 3.14 * radia
        print(f"perimeter:{perimeter}")


c1 = Circle(0, 0, 5)
c1.area_circle(0, 0, 5)
c1.perimeter(0, 0, 5)
