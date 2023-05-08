#this the code for shapes using class and object

import math


class AreaPerimeter():


    def triangle(self):
        a, b, c = map(int(input("Enter 3 sides\n").split()))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a)(s - b)(s - c))
        perimeter = a + b + c
        return area, perimeter

    def circle(self):
        radius = int(input("Enter the radius\n"))
        area = 3.14 * (radius * radius)
        perimeter = 2*3.14*radius
        return area, perimeter

    def square(self):
        side = int(input("Enter the side\n"))
        area = side * side
        perimeter = 4 * side
        return area, perimeter

    def rectangle(self):
        l, b = map(int(input("Enter length and breadth\n").split()))
        area = l * b
        perimeter = 2 * (l + b)
        return area, perimeter


shape = input("Enter the shape\n1.triangle\n2.Triangle\n3.Square\n4.Rectangle\n")
shape_object = AreaPerimeter()
if shape == "1":
    print(shape_object.triangle())
elif shape == "2":
    print(shape_object.circle())
elif shape == "3":
    print(shape_object.square())
elif shape == "4":
    print(shape_object.rectangle())
else:
    print("This is not supported")