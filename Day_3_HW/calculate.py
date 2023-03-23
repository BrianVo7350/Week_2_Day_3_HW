from math import pi

def square_footage_house(length, width):
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    square_footage = length * width
    return square_footage

print(square_footage_house(0,0))



def calculate_circumference():
    radius = float(input("enter radius: "))
    circumference = 2 * pi * radius
    return circumference

print(calculate_circumference())
