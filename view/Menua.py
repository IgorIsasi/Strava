import tkinter as tk
from tkinter import *
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
from view.EntrenamenduLeihoa import EntrenamenduLeihoa
from view import ScrollContainer
import os
dirname = os.path.dirname(__file__)



class Menua():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x650')
        self.window.title("Menua")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frames=[]
        aukerakMota=["Guztiak","Kayaking","Run","Ride","Rowing"]
        aldagaiaMota = StringVar(self.frameNagusia)
        aldagaiaMota.set(aukerakMota[0])
        motak = OptionMenu(self.frameNagusia, aldagaiaMota, aukerakMota[0], *aukerakMota)
        motak.pack()
        noiztik = tk.Entry(self.frameNagusia, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        noiztik.pack()
        nora = tk.Entry(self.frameNagusia, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        nora.pack()
        bilatu = Button(self.frameNagusia,text="Bilatu",command=lambda : self.entrenamenduakBilatu(noiztik.get(), nora.get(), aldagaiaMota.get()))
        bilatu.pack()
        self.window.mainloop()


    def entrenamenduakBilatu(self,noiztik,nora,mota):
        for frame in self.frames:
            frame.pack_forget()
            frame.grid_forget()
            frame.destroy()
        self.frames.clear()
        entrenamenduak = kudeatzaile.entrenamenduakBilatu(noiztik,nora,mota)
        for i in range(0,len(entrenamenduak)):
            self.frames.append(tk.Frame(self.frameNagusia,relief=RAISED,bd=4))
            self.frames[i].pack()
            #photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            #botoia=Button(frame, image = photo).pack()
            self.frames.append(Frame(self.frameNagusia))
            self.frames[i].pack()
            unekoEntrenamendua = entrenamenduak[i]
            izena = Button(self.frames[i],text=unekoEntrenamendua.izena,command=lambda : self.entrenamenduaBistaratu(unekoEntrenamendua))
            izena.pack()
            data = Label(self.frames[i],text=unekoEntrenamendua.hasieraData)
            data.pack()
            mota = Label(self.frames[i],text=unekoEntrenamendua.mota)
            mota.pack()
            distantzia = Label(self.frames[i],text=unekoEntrenamendua.distantzia)
            distantzia.pack()
            denbora = Label(self.frames[i],text=unekoEntrenamendua.denbora)
            denbora.pack()
            #print(unekoEntrenamendua.izena,unekoEntrenamendua.hasieraData,unekoEntrenamendua.mota,unekoEntrenamendua.distantzia,unekoEntrenamendua.denbora)
        

    def entrenamenduaBistaratu(self, entrenamendua):
        EntrenamenduLeihoa(entrenamendua)
