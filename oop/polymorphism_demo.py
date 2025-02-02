# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def calculate_area(shape: Shape):
    return shape.area()


def main():
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    print(f"Rectangle area: {calculate_area(rectangle)}")
    print(f"Circle area: {calculate_area(circle)}")


if __name__ == "__main__":
    main()