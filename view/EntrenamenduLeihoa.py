import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import RAISED
from view import ScrollContainer
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import os
dirname = os.path.dirname(__file__)


class EntrenamenduLeihoa():
    def __init__(self,entrenamendua):
        self.window = tk.Toplevel()
        self.window.geometry('660x500')
        self.window.title("Entrenamendua")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frameNagusia.grid_rowconfigure(1, weight=1)
        self.frameNagusia.grid_columnconfigure(1, weight=1)
        self.entrenamenduaErakutsi(entrenamendua)
        self.bueltakErakutsi(entrenamendua)

        self.window.mainloop()

    def entrenamenduaErakutsi(self,entrenamendua):
        frameID = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameID.grid()
        id = Label(frameID,text=f"ID: {entrenamendua.ID}")
        id.grid()
        frameIkus = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameIkus.grid()
        ikusgarritasuna = Label(frameIkus,text=f"Ikugarritasuna: {entrenamendua.ikusgarritasuna}")
        ikusgarritasuna.grid()
        frameIzena = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameIzena.grid()
        izena = Label(frameIzena,text=f"Izena: {entrenamendua.izena}")
        izena.grid()
        frameData = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameData.grid()
        data = Label(frameData,text=f"Data: {entrenamendua.hasieraData}")
        data.grid()
        frameMota = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameMota.grid()
        mota = Label(frameMota,text=f"Mota: {entrenamendua.mota}")
        mota.grid()
        frameDis = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameDis.grid()
        distantzia = Label(frameDis,text=f"Distantzia: {entrenamendua.distantzia}m")
        distantzia.grid()
        frameDenb = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameDenb.grid()
        denbora = Label(frameDenb,text=f"Denbora: {entrenamendua.denbora} segundu")
        denbora.grid()
        frameAbMax = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameAbMax.grid()
        abiaduraMax = Label(frameAbMax,text=f"AbiaduraMax: {entrenamendua.abiaduraMax}m/s")
        abiaduraMax.grid()
        frameAbBzb = tk.Frame(self.frameNagusia,relief=RAISED,bd=3,bg='yellow')
        frameAbBzb.grid()
        abiaduraBzb = Label(frameAbBzb,text=f"AbiaduraBzb: {entrenamendua.abiaduraBzb}m/s")
        abiaduraBzb.grid()



    def bueltakErakutsi(self,entrenamendua):
        bueltak = kudeatzaile.entrenamenduarenBueltakIkusi(entrenamendua)
        datuak = []
        for buelta in bueltak:
            datuak.append((buelta.izena, buelta.distantzia, buelta.denbora))

        goiburuak = ["Izena", "Distantzia", "Denbora"]
        taula = ttk.Treeview(self.frameNagusia, columns=(0,1,2), show='headings')

        for i,g in enumerate(goiburuak):
            taula.column(f"#{i}", minwidth=0, width=200)
            taula.heading(i, text=g)

        for i,d in enumerate(datuak):
            taula.insert(parent='', index=i, iid=i, values=d)
            
        taula.grid(pady=5)