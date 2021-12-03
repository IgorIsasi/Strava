import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import os
dirname = os.path.dirname(__file__)


class EkipamenduLeihoa:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('600x250')
        self.window.title("Ekipamenduak")
        #self.frameNagusia = Frame(self.window)
        datuak = []
        ekDatuak = []
        ekipamenduak = kudeatzaile.ekipamenduenDistantziaIkusi()
        for ekipamendu in ekipamenduak:
            ekDatuak.append(ekipamendu.izena)
            ekDatuak.append(ekipamendu.marka)
            ekDatuak.append(ekipamendu.modelo)
            ekDatuak.append(ekipamendu.distantzia)
            datuak.append(ekDatuak)
        goiburuak = ["Izena", "Marka", "Modeloa", "Distantzia"]
        taula = ttk.Treeview(self.window, columns=(0,1,2,3), show='headings')

        for i,g in enumerate(goiburuak):
            taula.column(f"#{i}", minwidth=0, width=100)
            taula.heading(i, text=g)

        for i,d in enumerate(datuak):
            taula.insert(parent='', index=i, iid=i, values=d)
            
        taula.pack()
        self.window.mainloop()