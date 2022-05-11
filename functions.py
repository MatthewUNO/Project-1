import math

def generate_rectangle(width_entry, length_entry, area_entry):
    '''
    Function to calculate the area of a rectangle
    :param width_entry:     - Input Shape Width
    :param length_entry:    - Input Shape Length
    :param area_entry:      - Output Shape Area
    '''
    try:
        result = float(width_entry.get()) * float(length_entry.get())   #Perfrom Math calculation
    except Exception as ex:                                             #Verify input
        print(ex)
        result = 'Invalid Input'

    area_entry.delete(1,'end')                                          #Clear any previous entry
    result_string = str(result)                                         #Convert result into a string
    area_entry.insert(0,result_string)                                  #Display shape area

def generate_triangle(base_entry, height_entry, area_entry):
    '''
      Function to calculate the area of a triangle
      :param base_entry:     - Input triangle Base
      :param height_entry:   - Input triangle Height
      :param area_entry:     - Output Shape Area
      '''
    try:
        result = float(base_entry.get()) * float(height_entry.get()) / 2    #Perfrom Math calculation
    except Exception as ex:                                                 #Verify input
        print(ex)
        result = 'Invalid Input'
    print(result)

    area_entry.delete(1, 'end')                                             #Clear any previous entry
    result_string = str(result)                                             #Convert result into a string
    area_entry.insert(0, result_string)                                     #Display shape area


def generate_square(square_entry, area_entry):
    '''
      Function to calculate the area of a square
      :param square_entry:    - Input length of a single side
      :param area_entry:      - Output Shape Area
      '''
    try:
        number = float(square_entry.get())                                  #Pull number from entry box
        result = number * number                                            #Perfrom Math calculation
    except Exception as ex:                                                 #Verify input
        print(ex)
        result = 'Invalid Input'
    print(result)

    area_entry.delete(0, 'end')                                             #Clear any previous entry
    result_string = str(result)                                             #Convert result into a string
    area_entry.insert(0, result_string)                                     #Display shape area

def generate_circle(radius_entry, area_entry):
    '''
      Function to calculate the area of a circle
      :param radius_entry:     - Input circle radius
      :param area_entry:      - Output Shape Area
      '''
    try:
        area = math.pi * float(radius_entry.get()) ** 2                     #Perfrom Math calculation
        result = "{:.2f}".format(area)                                      #Format result to two decimals
    except Exception as ex:                                                 #Verify input
        print(ex)
        result = 'Invalid Input'
    print(result)
    area_entry.delete(1, 'end')                                             #Clear any previous entry
    result_string = str(result)                                             #Convert result into a string
    area_entry.insert(0, result_string)                                     #Display shape area