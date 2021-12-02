import tkinter as tk
from tkinter import messagebox
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import os
dirname = os.path.dirname(__file__)


class EntrenamenduLeihoa():
    def __init__(self,entrenamendua):
        self.window = tk.Toplevel()
        self.window.geometry('400x400')
        self.window.title("Entrenamendua")
        id = Label(self.window,text=entrenamendua.ID)
        id.pack()
        ikusgarritasuna = Label(self.window,text=entrenamendua.ikusgarritasuna)
        ikusgarritasuna.pack()
        izena = Label(self.window,text=entrenamendua.izena)
        izena.pack()
        data = Label(self.window,text=entrenamendua.hasieraData)
        data.pack()
        mota = Label(self.window,text=entrenamendua.mota)
        mota.pack()
        distantzia = Label(self.window,text=entrenamendua.distantzia)
        distantzia.pack()
        denbora = Label(self.window,text=entrenamendua.denbora)
        denbora.pack()
        abiaduraMax = Label(self.window,text=entrenamendua.abiaduraMax)
        abiaduraMax.pack()
        abiaduraBzb = Label(self.window,text=entrenamendua.abiaduraBzb)
        abiaduraBzb.pack()