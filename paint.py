import tkinter as tk 
from tkinter.colorchooser import askcolor

class Paint(object):
    DEFAULT_COLOR="black"
    DEFAULT_PEN_SIZE=5.0
    
    def __init__(self):
        
        self.root=tk.Tk()
        
        self.pen_button=tk.Button(self.root, text="pen", command=self.use_pen)
        self.pen_button.grid(row=0, colum=0)
        
        self.brush_button=tk.Button(self.root, text="brush", command=self.use_brush)
        self.brush_button.grid(row=0, colum=1)
        
        self.color_button=tk.Button(self.root, text="color", command=self.use_color)
        self.color_button.grid(row=0, colum=2)
        
        self.eraser_button=tk.Button(self.root, text="eraser", command=self.use_eraser)
        self.eraser_button.grid(row=0, colum=3)
        
        self.choose_size_button=tk.Scale(self.root, from_=1, to=10, orient=tk.HORIZANTAL)
        self.choose_size_button.grid(row=0, column=4)
        
        self.c=tk.Canvas(self.root, bg="white", width=600, height=600)
        self.c.grid( row = 1, columnspan=5)
        
        self.setup()
        self.root_mainloop() 
        def setup(self): 
            self.old_x=None
            self.old_y=None            
            self.line_width=self.choose_size_button.get()
            self.color=self.DEFAULT_COLOR
            self.eraser_on=False
            self.c.bind("<B1-Motion>", self.paint)
            self.c.bind("<ButtonRelease-1>", self.reset)
        
        def use_pen(self):
            self.active_button(self.pen_button)
        
        def use_brush(self):
            self.active_button(self.brush_button)
            
        def use_eraser(self):
            self.active_button(self.eraser_button, eraser_mode=True)
            
        def choose_color(self):
            self.eraser_on=False
            self.color=askcolor(color=self.color)[1]
            
        
        def active_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=tk.RAISED)
            some_button.config(reilef=tk.SUNKEN)
            self.active_button=some_button
            self.eraser_on=eraser_mode
            
        def paint(self, event):
            paint_color= "white" if self.eraser_on else self.color
            self.line_width= self.choose_size_button.get()
            
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.line_width, fill=paint_color, 
                                   capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
            self.old_x=event.x
            self.old_y=event.y
        def reset(self,event):
            self.old_x=None
            self.old_y=None
        
               
        

if __name__ == "__main__":
    
    Paint()
