class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__area = 0
        self.__perimeter = 0

    def rect_info(self):
        self.__area = self._length * self._width
        self.__perimeter = 2 * (self._length + self._width)
        print(f"area={self.__area},perimeter={self.__perimeter},length={self._length},width={self._width}")


class Parallelepiped(Rectangle):
    def __init__(self, length, width, heigth):
        Rectangle.__init__(self, length, width)
        self.__heigth = heigth
        self.__volume = 0

    def parallelepiped_volume(self):
        self.__volume = self._length * self._width * self.__heigth
        print(f"volume={self.__volume}")


rec = Rectangle(2, 3)
rec.rect_info()
pal=Parallelepiped(2,3,5)
pal.parallelepiped_volume()