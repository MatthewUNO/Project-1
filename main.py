from tkinter import *
from functions import *
from gui import *

def main():
   
    window = Tk()
    window.title('Project 1')
    window.geometry('510x400')
    #window.resizable(False, False)
    Label(window, text='------------------------------------------ \n'
                       'Select Shape\n'
                       '------------------------------------------').pack()
    
    widgets = GUI(window)
    window.mainloop()

def rectangle():
   
    width = StringVar()
    length = StringVar()
    area = StringVar()
    
    rectangle_window = Toplevel()
    rectangle_window.title("Rectangle")
    rectangle_window.geometry("600x300")
    Label(rectangle_window, text='------------------------------------------ \n'
                                 'Enter Length and Width of Rectangle\n'
                                 '------------------------------------------').pack()
    
    width_frame = Frame(rectangle_window)
    width_label = Label(width_frame, text='Width: ')
    width_frame.pack(anchor='w', padx=200, pady=10)
    width_label.pack(side='left')    
    width_entry = Entry(width_frame)
    width_entry.pack(padx=5, side='left')
    
    length_frame = Frame(rectangle_window)
    length_label = Label(length_frame, text='Length:')
    length_frame.pack(anchor='w', padx=200, pady=10)
    length_label.pack(side='left')    
    length_entry = Entry(length_frame)
    length_entry.pack(padx=5, side='left')
        
    area_frame = Frame(rectangle_window)
    area_label = Label(area_frame, text='Area: ')
    area_frame.pack(anchor='w', padx=200, pady=10)
    area_label .pack(side='left')    
    """
    area_entry = Entry(area_frame)
    area_entry.pack(padx=5, side='left')
    """
    
    #Create Start Button
    generate_area = Button(rectangle_window, text='Generate', command=run)
    generate_area.pack(padx=20, side='left')
    area_label = Label(area_frame, text='Area: result')
    close_rectangle = Button(rectangle_window, text='Close')
    close_rectangle.pack(padx=20, side='right')


def triangle():
        triangle_window = Toplevel()
        triangle_window.title("Triangle")
        triangle_window.geometry("500x400")
        Label(triangle_window, text='------------------------------------------ \n'
                                  'Enter Base and Height of Triangle\n'
                                  '------------------------------------------').pack()
        
def square():
        square_window = Toplevel()
        square_window.title("Square")
        square_window.geometry("500x400")
        Label(square_window, text='------------------------------------------ \n'
                                  'Enter Length of Side\n'
                                  '------------------------------------------').pack()
        
def circle():
        circle_window = Toplevel()
        circle_window.title("Circle")
        circle_window.geometry("500x400")
        Label(circle_window, text='------------------------------------------ \n'
                                  'Enter Circle Radius\n'
                                  '------------------------------------------').pack()

def run():
    width = float(width_entry.get())
    length = float(length_entry.get())
    rectangle_area()
    
    area_frame = Frame(rectangle_window)
    area_label = Label(area_frame, text='Area:')
    #Label('{:.2f}'.format(functions.rectangle_area()))
    area_frame.pack(anchor='w', padx=200, pady=10)
    area_label.pack(side='left')


def generate():
    try:
        result = float(width.get()) * float(length.get())
    except Exception as ex:
        print(ex)
        result = 'error'
        
    return result
        


if __name__ == '__main__':
    main()