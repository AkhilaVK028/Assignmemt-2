#this the python code for shapes
import math

def area_perimeter_of_rectangle(height, width):
    area_of_rectangle= height * width
    perimeter_of_rectangle= 2*(height+width)
    return area_of_rectangle,perimeter_of_rectangle

def area_perimeter_of_square(sides):
    area_of_square= sides * sides
    perimeter_of_square= 4 * sides
    return area_of_square,perimeter_of_square

def area_perimeter_of_circle(radius):
    area_of_circle=math.pi * radius * radius
    perimeter_of_circle=2 * math.pi * radius
    return area_of_circle,perimeter_of_circle


def main():
    shape=input("enter the shape(rectangle,square,circle): ")


    if shape == "rectangle":
        height=int(input("enter the height:"))
        width=int(input("enter the width:"))
        print(area_perimeter_of_rectangle(height,width))


    elif shape=="square"  :
        sides=int(input("enter the side of the square:"))
        print(area_perimeter_of_square(sides))

    elif shape=="circle" :
        radius=int(input("enter the radius of the circle:"))
        print(area_perimeter_of_circle(radius))

    else:
        print("invalid shape entered")
# calling the main
#if __name__=='__name__':
main()




