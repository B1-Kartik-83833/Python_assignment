class Product:
    def __init__(self, pid, manufacture_location):
        self.__pid = pid
        self.__manufacture_location = manufacture_location

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_manufacture_location(self):
        return self.__manufacture_location

    def set_manufacture_location(self, manufacture_location):
        self.__manufacture_location = manufacture_location

    def __str__(self):
        return f"Product ID: {self.__pid}, Manufacture Location: {self.__manufacture_location}"

    def print_data(self):
        print(self.__str__())


class Book:
    def __init__(self, name, number_of_pages, author, price):
        self.__name = name
        self.__number_of_pages = number_of_pages
        self.__author = author
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        self.__number_of_pages = number_of_pages

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price <= 0:
            print("Price is not valid.")
        else:
            self.__price = price

    def __str__(self):
        return f"Book: {self.__name}, Author: {self.__author}, Pages: {self.__number_of_pages}, Price: {self.__price}"

    def print_data(self):
        print(self.__str__())


product1 = Product("product", "pune")
book1 = Book("book1", 34, "XYZ", 1000)

product1.print_data()
book1.print_data()

book1.set_price(-10)
book1.set_price(0)
book1.set_price(19.99)
