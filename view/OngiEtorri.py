import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from controllers.DBKudeatzailea.DBKud import kudeatzaile
from view.Menua import Menua
from view import ScrollContainer
import os
dirname = os.path.dirname(__file__)

class OngiEtorri():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('470x530')
        self.window.title("Ongi etorri")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        testua = Label(self.frameNagusia,text="Kaixo!",font=("Times New Roman",25))
        testua.grid(column=1)
        irudia = Image.open(f"{dirname}/irudiak/IMG_strava.png")
        irudia = irudia.resize((450,400))
        irudiaTk = ImageTk.PhotoImage(irudia)
        panel = Label(self.frameNagusia, image = irudiaTk)
        panel.grid(column=1)
        botoia = Button(self.frameNagusia,text="Sartu", command=self.datuakKargatu)
        botoia.grid(column=1, pady=5)
        egileak = Label(self.frameNagusia,text="Egileak: Julen Fuentes, Markel Rubiños eta Igor Isasi")
        egileak.grid(column=1)
        self.window.mainloop()

    def datuakKargatu(self):
        kudeatzaile.kargatuDB()
        tk.messagebox.showinfo(title="Datuak kargatuta", message="Datuak ongi kargatu dira!")
        self.window.destroy()
        Menua()
        

