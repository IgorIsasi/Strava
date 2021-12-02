import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import os
dirname = os.path.dirname(__file__)



class Menua():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x500')
        self.window.title("Menua")

        

        for i in range(0,5):
            frame=tk.Frame(self.window)
            frame.pack()

            photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            botoia=Button(frame, image = photo).pack()
            testua=tk.Label(frame,text="Datuak ").pack()


        
        


    
        
        
        self.window.mainloop()
