class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
# membuat objek dari class Rectangle
rect = Rectangle(5, 10)

# memanggil method area dan method perimeter dari objek Rectangle
print("Luas persegi panjang:", rect.area())
print("Keliling persegi panjang:", rect.perimeter())

# membuat objek dari class Circle
Circle = Circle(8)

# memanggil method area dan men=thod perimeter dari objek Circle
print("Luas lingkaran:", Circle.area())
print("Keliling lingkaran:", Circle.perimeter())
