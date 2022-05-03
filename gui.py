from tkinter import *
from csv import *
from main import *
#from main_copy import *

class GUI:
    
    def __init__(self, window):
        self.window = window
        '''
        #Create Frame for Name
        #self.frame_intro1 = Frame(self.window)
        self.label_intro1 = Label(self.frame_intro1, text=('------------------------------------------ \n'
                                                           'Select Shape\n'
                                                           '------------------------------------------'))
       # self.entry_intro1 = Entry(self.frame_intro1)
       # self.label_intro1.pack(padx=5, side='left')
        #self.entry_name.pack(padx=5, side='left')
       # self.frame_intro1.pack(anchor='n', pady=10)   # anchor='n' holds frame position in the center.
        
       '''
        
        #Create Frame for Status
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.frame4 = Frame(self.window)
        #self.label_status = Label(self.frame_status, text='Status')

        
        #Create Radio Options
        self.radio_1 = IntVar()
        self.radio_1.set(None)
        
        self.radio_rectangle = Radiobutton(self.frame1, text='Rectangle', variable=self.radio_1, value=1, command= rectangle)     
        self.radio_triangle = Radiobutton(self.frame2, text='Triangle', variable=self.radio_1, value=2, command= triangle)
        self.radio_square = Radiobutton(self.frame3, text='Square', variable=self.radio_1, value=3, command= square)
        self.radio_circle = Radiobutton(self.frame4, text='Circle', variable=self.radio_1, value=4, command= circle)
        
        #self.label_status.pack(padx=5, side='left')
        self.frame1.pack(anchor='w', padx=200, pady=10)    # anchor='w' holds frame position to the left.
        self.frame2.pack(anchor='w', padx=200, pady=10)
        self.frame3.pack(anchor='w', padx=200, pady=10)
        self.frame4.pack(anchor='w', padx=200, pady=10)
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle.pack(side='left')
        
        #Create Start Button
        self.button_close = Button(self.window, text='Close')
        self.button_close.pack(padx=20, side='right')
        
    def clicked(self):
        
       # name = self.entry_name.get()
       # age = int(self.entry_age.get())
       # age = age * 2
        
        #Find Chosen Status
        status = self.radio_1.get()
        if status == 1:
            status = 'Student'
        elif status == 2:
            status = 'Staff'
        else:
            status = 'Both'
            
    
    