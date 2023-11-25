# Overloading
class MathOperation:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Penggunaan
obj = MathOperation()
print(obj.add(2, 3))      # Memanggil metode pertama
print(obj.add(2, 3, 4))   # Memanggil metode kedua

# Overriding
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Penggunaan
square_obj = Square(5)
circle_obj = Circle(3)

print(square_obj.area())  # Memanggil metode area() dari kelas Square
print(circle_obj.area())  # Memanggil metode area() dari kelas Circle