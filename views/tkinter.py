from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class window(tk.Tk):
    
    def change_theme(self):
        if not self.toogle:
           
            self.chan_theme.configure(image=self.on)
            self["bg"]="#000000"
            self.chan_theme.configure(background="#000000")
            self.toogle=True
        else:
            self.update()
            
            self.chan_theme.configure(image=self.off)
            self.chan_theme.configure(background="#ffffff")
            self["bg"]="#ffffff"
            self.toogle=False
            
    
    def __init__(self):
        
        
    
     
     super().__init__()
     
     self.toogle=False
     
     self.geometry("400x400")
     
     self.title("Test")
     
     self.attributes("-topmost",True)
     
     self.resizable(0,0)
     
     ##
     self.on=Image.open("flet-routing-tutorial//assets//on.PNG").resize((30,30))
     self.on=ImageTk.PhotoImage(self.on)
     self.off=Image.open("flet-routing-tutorial//assets//off.PNG").resize((30,30))
     self.off=ImageTk.PhotoImage(self.off)
     ##
     
     
     self.chan_theme=tk.Button(image=self.off,bd=0,command=self.change_theme)
     self.chan_theme.place(x=50,y=50)
     self.chan_theme.configure(image=self.off)
     
     
# app=window()
# app.mainloop()
        