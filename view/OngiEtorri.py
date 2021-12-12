import tkinter as tk
from PIL import ImageTk, Image
from controllers.DBKudeatzailea.DBKud import kudeatzaile
from view.Menua import Menua
from view import ScrollContainer
import os
dirname = os.path.dirname(__file__)

class OngiEtorri():
    def __init__(self):
        self.window = tk.Tk()
        leihoZabalera = 470
        leihoAltuera = 530
        x = (self.window.winfo_screenwidth() // 2) - (leihoZabalera // 2)
        y = (self.window.winfo_screenheight() // 2) - (leihoAltuera // 2)
        self.window.geometry('{}x{}+{}+{}'.format(leihoZabalera, leihoAltuera, x, y))
        self.window.title("Ongi etorri")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        testua = tk.Label(self.frameNagusia,text="Kaixo!",font=("Times New Roman",25))
        testua.grid(column=1)
        irudia = Image.open(f"{dirname}/irudiak/IMG_strava.png")
        irudia = irudia.resize((450,400))
        irudiaTk = ImageTk.PhotoImage(irudia)
        panel = tk.Label(self.frameNagusia, image = irudiaTk)
        panel.grid(column=1)
        botoia = tk.Button(self.frameNagusia,text="Sartu", command=self.datuakKargatu)
        botoia.grid(column=1, pady=5)
        egileak = tk.Label(self.frameNagusia,text="Egileak: Julen Fuentes, Markel Rubiños eta Igor Isasi")
        egileak.grid(column=1)
        self.window.mainloop()

    def datuakKargatu(self):
        kudeatzaile.kargatuDB()
        tk.messagebox.showinfo(title="Datuak kargatuta", message="Datuak ongi kargatu dira!")
        self.window.destroy()
        Menua()
        

