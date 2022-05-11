from tkinter import *
from functions import *
from gui import *

def main():
    '''
    Function to crete the primary graphical window.
    '''
    window = Tk()
    window.title('Project 1')
    window.geometry('510x300')
    window.resizable(False, False)
    Label(window, text='------------------------------------------ \n'
                       'Select Shape\n'
                       '------------------------------------------').pack()
    
    widgets = GUI(window)
    window.mainloop()

def rectangle():
    '''
    Fucntion to create an additional window whenever rectangle is selected.
    '''
    rectangle_window = Toplevel()
    rectangle_window.title("Rectangle")
    rectangle_window.geometry("600x300")
    rectangle_window.resizable(False, False)
    Label(rectangle_window, text='------------------------------------------ \n'
                                 'Enter Length and Width of Rectangle\n'
                                 '------------------------------------------').pack()

    #Creates Width Input Box
    width_frame = Frame(rectangle_window)
    width_label = Label(width_frame, text='Width: ')
    width_frame.pack(anchor='w', padx=200, pady=10)
    width_label.pack(side='left')    
    width_entry = Entry(width_frame)
    width_entry.pack(padx=5, side='left')

    #Creates Length Input box
    length_frame = Frame(rectangle_window)
    length_label = Label(length_frame, text='Length:')
    length_frame.pack(anchor='w', padx=200, pady=10)
    length_label.pack(side='left')    
    length_entry = Entry(length_frame)
    length_entry.pack(padx=5, side='left')

    #Creates Area Output Box
    area_frame = Frame(rectangle_window)
    area_label = Label(area_frame, text='Rectangle Area: ')
    area_frame.pack(anchor='w', padx=155, pady=10)
    area_label.pack(side='left')
    area_entry = Entry(area_frame)
    area_entry.pack(padx=5, side='left')

    #Creates Button to Perform Calculation Function
    generate_area = Button(rectangle_window, text='Generate', command= lambda: generate_rectangle(width_entry, length_entry, area_entry))
    generate_area.pack(padx=20, side='left')

    #Creates Button to close the current window
    close_rectangle = Button(rectangle_window, text='Close', command=rectangle_window.destroy)
    close_rectangle.pack(padx=20, side='right')


def triangle():
        '''
        Fucntion to create an additional window whenever triangle is selected.
        '''
        triangle_window = Toplevel()
        triangle_window.title("Triangle")
        triangle_window.geometry("600x300")
        triangle_window.resizable(False, False)
        Label(triangle_window, text='------------------------------------------ \n'
                                  'Enter Base and Height of Triangle\n'
                                  '------------------------------------------').pack()

        #Creates Base Input Box
        base_frame = Frame(triangle_window)
        base_label = Label(base_frame, text='Width: ')
        base_frame.pack(anchor='w', padx=200, pady=10)
        base_label.pack(side='left')
        base_entry = Entry(base_frame)
        base_entry.pack(padx=5, side='left')

        #Creates Height Input Box
        height_frame = Frame(triangle_window)
        height_label = Label(height_frame, text='Height:')
        height_frame.pack(anchor='w', padx=200, pady=10)
        height_label.pack(side='left')
        height_entry = Entry(height_frame)
        height_entry.pack(padx=5, side='left')

        #Creates Area Output Box
        area_frame = Frame(triangle_window)
        area_label = Label(area_frame, text='Triangle Area: ')
        area_frame.pack(anchor='w', padx=165, pady=10)
        area_label.pack(side='left')
        area_entry = Entry(area_frame)
        area_entry.pack(padx=5, side='left')

        #Creates Button to Perform Calculation Function
        generate_area = Button(triangle_window, text='Generate', command=lambda: generate_triangle(base_entry, height_entry, area_entry))
        generate_area.pack(padx=20, side='left')
        area_label = Label(area_frame, text='Area: result')

        #Creates Button to close the current window
        close_triangle = Button(triangle_window, text='Close', command=triangle_window.destroy)
        close_triangle.pack(padx=20, side='right')

def square():
        '''
        Fucntion to create an additional window whenever square is selected.
        '''
        square_window = Toplevel()
        square_window.title("Square")
        square_window.geometry("600x250")
        square_window.resizable(False, False)
        Label(square_window, text='------------------------------------------ \n'
                                  'Enter Length of Side\n'
                                  '------------------------------------------').pack()

        #Creates Side Length Input Box
        square_frame = Frame(square_window)
        square_label = Label(square_frame, text='Side: ')
        square_frame.pack(anchor='w', padx=200, pady=10)
        square_label.pack(side='left')
        square_entry = Entry(square_frame)
        square_entry.pack(padx=5, side='left')

        # Creates Area Output Box
        area_frame = Frame(square_window)
        area_label = Label(area_frame, text='Square Area: ')
        area_frame.pack(anchor='w', padx=160, pady=10)
        area_label.pack(side='left')
        area_entry = Entry(area_frame)
        area_entry.pack(padx=5, side='left')

        #Creates Button to Perform Calculation Function
        generate_area = Button(square_window, text='Generate', command=lambda: generate_square(square_entry, area_entry))
        generate_area.pack(padx=20, side='left')
        area_label = Label(area_frame, text='Area: result')

        #Creates Button to close the current window
        close_square = Button(square_window, text='Close', command=square_window.destroy)
        close_square.pack(padx=20, side='right')

def circle():
        '''
        Fucntion to create an additional window whenever circle is selected.
        '''
        circle_window = Toplevel()
        circle_window.title("Circle")
        circle_window.geometry("600x250")
        circle_window.resizable(False, False)
        Label(circle_window, text='------------------------------------------ \n'
                                  'Enter Circle Radius\n'
                                  '------------------------------------------').pack()

        # Creates Radius Input Box
        radius_frame = Frame(circle_window)
        radius_label = Label(radius_frame, text='Radius: ')
        radius_frame.pack(anchor='w', padx=200, pady=10)
        radius_label.pack(side='left')
        radius_entry = Entry(radius_frame)
        radius_entry.pack(padx=5, side='left')

        # Creates Area Output Box
        area_frame = Frame(circle_window)
        area_label = Label(area_frame, text='Circle Area: ')
        area_frame.pack(anchor='w', padx=180, pady=10)
        area_label.pack(side='left')
        area_entry = Entry(area_frame)
        area_entry.pack(padx=5, side='left')

        #Creates Button to Perform Calculation Function
        generate_area = Button(circle_window, text='Generate', command=lambda: generate_circle(radius_entry, area_entry))
        generate_area.pack(padx=20, side='left')
        area_label = Label(area_frame, text='Area: result')

        #Creates Button to close the current window
        close_circle = Button(circle_window, text='Close', command=circle_window.destroy)
        close_circle.pack(padx=20, side='right')

if __name__ == '__main__':
    main()