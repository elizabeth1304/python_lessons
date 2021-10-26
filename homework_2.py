import math
import abc
from abc import ABC


class Shape(ABC):

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    current_instance_count: int = 0

    def __new__(cls, *args, **kwargs):
        cls.current_instance_count += 1
        return super().__new__(cls)

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = self.int_validation(side_a)
        self.side_b = self.int_validation(side_b)
        self.side_c = self.int_validation(side_c)

    @staticmethod
    def int_validation(value):
        if isinstance(value, (int, float)):
            if value <= 0:
                raise ValueError("Can't be negative or Zero")
        else:
            raise ValueError("Must be an instance of int or float")

        return value

    @classmethod
    def get_current_instance_count(cls):
        return f"Current instance count is {cls.current_instance_count}"

    def __repr__(self):
        return f'Sides of a Trianle - {self.side_a}, {self.side_b}, {self.side_c}'

    def area(self):
        p: int = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("not comparable")

        return self.perimeter() == other.perimeter()



triangle_1 = Triangle(3, 4, 5)
triangle_2 = Triangle(5, 4, 3)
print(triangle_1.get_current_instance_count())
print(triangle_1 == triangle_2)
print(triangle_1.area())
print(triangle_1.perimeter())


class Cube:
    def __init__(self, radius):
        self.radius = self.number_validation(radius)

    @staticmethod
    def number_validation(value):
        if type(value) == str:
            raise ValueError("Wrong Value")
        else:
            return value

    def __repr__(self):
        return f'Radius of a Cube - {self.radius}'

    def area_of_cube(self):
        area = 6 * self.radius * self.radius
        return f'Area of Cube - {area}'

    def volume_of_cube(self):
        volume = self.radius * self.radius * self.radius
        return f'Volume of cube {volume}'

    def __eq__(self, other):
        if not isinstance(other, Cube):
            raise ValueError("not comparable")

        return self.area_of_cube() == other.area_of_cube()

    def __gt__(self, other):
        if not isinstance(other, Cube):
            raise ValueError("Comparetion can be done between same type of objects.")

        return self.area_of_cube() > other.area_of_cube()

cube_1 = Cube(5)
cube_2 = Cube(5)
print(cube_1.volume_of_cube())
print(cube_1 > cube_2)
print(cube_1 == cube_2)

class Rectangular:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def to_tuple(self):
        return self.side1, self.side2, self.side3

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise ValueError("Can't compare not Rectangular objects.")

        comparison = sorted(self.to_tuple()) == sorted(other.to_tuple())

        return comparison

    def __lt__(self, other):
        self_sorted = sorted(self.to_tuple())
        other_sorted = sorted(other.to_tuple())
        comparison = True
        for i in range(3):
            check = self_sorted[i] >= other_sorted[i]
            if check:
                comparison = False
                break
        return comparison


rect_1 = Rectangular(1, 5, 8)
rect_2 = Rectangular(5, 1, 8)

print(rect_1 == rect_2)
print(rect_1 < rect_2)
