class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 6)
print("Luas persegi panjang:", rect.area())  # Output: Luas persegi panjang: 30

circle = Circle(4)
print("Luas lingkaran:", circle.area())  # Output: Luas lingkaran: 50.24
