import tkinter as tk
from tkinter import messagebox
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
from view.EntrenamenduLeihoa import EntrenamenduLeihoa
import os
dirname = os.path.dirname(__file__)



class Menua():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x600')
        self.window.title("Menua")
        entrenamenduak = kudeatzaile.entrenamenduakIkusi()

        for i in range(0,len(entrenamenduak)):
            frame=tk.Frame(self.window,relief=RAISED,bd=4)
            frame.pack()
            #photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            #botoia=Button(frame, image = photo).pack()
            unekoEntrenamendua = entrenamenduak[i]
            izena = Button(frame,text=unekoEntrenamendua.izena,command=lambda : self.entrenamenduaBistaratu(unekoEntrenamendua))
            izena.pack()
            data = Label(frame,text=unekoEntrenamendua.hasieraData)
            data.pack()
            mota = Label(frame,text=unekoEntrenamendua.mota)
            mota.pack()
            distantzia = Label(frame,text=unekoEntrenamendua.distantzia)
            distantzia.pack()
            denbora = Label(frame,text=unekoEntrenamendua.denbora)
            denbora.pack()
            #print(unekoEntrenamendua.izena,unekoEntrenamendua.hasieraData,unekoEntrenamendua.mota,unekoEntrenamendua.distantzia,unekoEntrenamendua.denbora)

        self.window.mainloop()


    def entrenamenduaBistaratu(self, entrenamendua):
        EntrenamenduLeihoa(entrenamendua)
