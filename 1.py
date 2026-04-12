class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3.5)


print("Фігура 1 (10x5):")
print(f"Площа: {rect1.area()}")
print(f"Периметр: {rect1.perimeter()}")

print("-" * 20)


print("Фігура 2 (7x3.5):")
print(f"Площа: {rect2.area()}")
print(f"Периметр: {rect2.perimeter()}")