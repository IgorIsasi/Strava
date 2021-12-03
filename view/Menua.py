import tkinter as tk
from tkinter import *
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
from view.EntrenamenduLeihoa import EntrenamenduLeihoa
from view.EkipamenduLeihoa import EkipamenduLeihoa
from view import ScrollContainer
import os
dirname = os.path.dirname(__file__)



class Menua():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('350x700')
        self.window.title("Menua")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frames=[]
        botoiakFrame = Frame(self.frameNagusia)
        botoiakFrame.pack()
        eguneratu = Button(botoiakFrame,text="Datuak eguneratu",command=lambda : self.datuakEguneratu())
        eguneratu.pack()
        ekipamendua = Button(botoiakFrame,text="Ekipamenduak erakutsi",command=lambda : self.ekipamenduakErakutsi())
        ekipamendua.pack()
        bilaketaFrame = Frame(self.frameNagusia)
        bilaketaFrame.pack()
        aukerakMota=["Guztiak","Kayaking","Run","Ride","Rowing"]
        aldagaiaMota = StringVar(bilaketaFrame)
        aldagaiaMota.set(aukerakMota[0])
        motak = OptionMenu(bilaketaFrame, aldagaiaMota, aukerakMota[0], *aukerakMota)
        motak.pack()
        noiztik = tk.Entry(bilaketaFrame, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        noiztik.pack()
        nora = tk.Entry(bilaketaFrame, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        nora.pack()
        bilatu = Button(bilaketaFrame,text="Bilatu",command=lambda : self.entrenamenduakBilatu(noiztik.get(), nora.get(), aldagaiaMota.get()))
        bilatu.pack()
        self.window.mainloop()


    def datuakEguneratu(self):
        kudeatzaile.kargatuDB()
        tk.messagebox.showinfo(title="Datuak eguneratuta", message="Datuak ongi eguneratu dira!")

    def ekipamenduakErakutsi(self):
        EkipamenduLeihoa()

    def entrenamenduakBilatu(self,noiztik,nora,mota):
        for frame in self.frames:
            frame.grid_forget()
            frame.destroy()
        self.frames.clear()
        entrenamenduak = kudeatzaile.entrenamenduakBilatu(noiztik,nora,mota)
        for i in range(0,len(entrenamenduak)):
            self.frames.append(tk.Frame(self.frameNagusia,relief=RAISED,bd=4))
            self.frames[i].pack()
            #photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            #botoia=Button(frame, image = photo).pack()
            unekoEntrenamendua = entrenamenduak[i]
            izena = Button(self.frames[i],text=unekoEntrenamendua.izena,command=lambda i=i: self.entrenamenduaBistaratu(unekoEntrenamendua))
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
