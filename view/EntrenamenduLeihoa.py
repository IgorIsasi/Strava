import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import os
dirname = os.path.dirname(__file__)


class EntrenamenduLeihoa():
    def __init__(self,entrenamendua):
        self.window = tk.Toplevel()
        self.window.geometry('900x400')
        self.window.title("Entrenamendua")

        self.entrenamenduaErakutsi(entrenamendua)
        self.bueltakErakutsi(entrenamendua)

        self.window.mainloop()

    def entrenamenduaErakutsi(self,entrenamendua):
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



    def bueltakErakutsi(self,entrenamendua):
        bueltak = kudeatzaile.entrenamenduarenBueltakIkusi(entrenamendua)
        datuak = []
        for buelta in bueltak:
            datuak.append(buelta.izena)
            datuak.append(buelta.distantzia)
            datuak.append(buelta.denbora)
            print(buelta.izena,buelta.distantzia,buelta.denbora)

        goiburuak = ["Izena", "Distantzia", "Denbora"]
        taula = ttk.Treeview(self.window, columns=(0,1,2), show='headings')

        for i,g in enumerate(goiburuak):
            taula.column(f"#{i}", minwidth=0, width=300)
            taula.heading(i, text=g)

        for i,d in enumerate(datuak):
            taula.insert(parent='', index=i, iid=i, values=d)
            
        taula.pack()