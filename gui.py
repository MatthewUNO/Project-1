from tkinter import *
from main import *

class GUI:
    '''
    Class to maintain the primary window of the application
    '''
    def __init__(self, window):
        self.window = window
        
        #Create Frames for user to select desired shape
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.frame4 = Frame(self.window)

        #Assign RadioButton Options
        self.radio_1 = IntVar()
        self.radio_1.set(None)
        
        self.radio_rectangle = Radiobutton(self.frame1, text='Rectangle', variable=self.radio_1, value=1, command= rectangle)
        self.radio_triangle = Radiobutton(self.frame2, text='Triangle', variable=self.radio_1, value=2, command= triangle)
        self.radio_square = Radiobutton(self.frame3, text='Square', variable=self.radio_1, value=3, command= square)
        self.radio_circle = Radiobutton(self.frame4, text='Circle', variable=self.radio_1, value=4, command= circle)
        
        #Anchor RadioButtons within the graphical window
        self.frame1.pack(anchor='w', padx=200, pady=10)    # anchor='w' holds frame position to the left.
        self.frame2.pack(anchor='w', padx=200, pady=10)
        self.frame3.pack(anchor='w', padx=200, pady=10)
        self.frame4.pack(anchor='w', padx=200, pady=10)
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle.pack(side='left')
        
        #Create Application Close Button
        self.button_close = Button(self.window, text='Close', command=window.destroy)
        self.button_close.pack(padx=20, side='right')