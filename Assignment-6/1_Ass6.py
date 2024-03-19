class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self._mileage = mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        Vehicle.__init__(self, max_speed, mileage)

    def print_info(self):
        print(f"max speed:{self._max_speed},mileage:{self._mileage}")


b1 = Bus(120, 50)
b1.print_info()
