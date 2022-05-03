import math
#from main import *

# Circle Function
def circle_area(radius):
    if type(radius) != int and type(radius) != float:
        raise TypeError('Input is not a numeric value')

    if radius <= 0:
        raise ValueError('Radius is not a positive number')
    return math.pi * radius ** 2

# Rectangle Function
def rectangle_area():
    
    #width = float(rectangle(width_entry).get())
    #length = float(rectangle(length_entry).get())
    
    if type(length) != int and type(length) != float:
        raise TypeError('Length is not a numeric value')
    
    if type(width) != int and type(width) != float:
        raise TypeError('Width is not a numeric value')

    if length <= 0:
        raise ValueError('Length input is not a positive number')
    
    if width <= 0:
        raise ValueError('Width input is not a positive number')
    
    #return length * width
    area.set(result)

# Square Function
def square_area(side):
    if type(side) != int and type(side) != float:
        raise TypeError('Side is not a numeric value')

    if side <= 0:
        raise ValueError('Side input is not a positive number')
    return side * side

# Triangle Function
def triangle_area(base, height):
    if type(base) != int and type(base) != float:
        raise TypeError('Base is not a numeric value')
    
    if type(height) != int and type(height) != float:
        raise TypeError('Height is not a numeric value')

    if base <= 0:
        raise ValueError('Base input is not a positive number')
    
    if height <= 0:
        raise ValueError('Height input is not a positive number')
    
    return base * height / 2


