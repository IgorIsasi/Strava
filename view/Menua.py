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
        self.window.geometry('705x530')
        self.window.title("Menua")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frameNagusia.grid_rowconfigure(1, weight=1)
        self.frameNagusia.grid_columnconfigure(1, weight=1)
        self.frames=[]
        botoiakFrame = Frame(self.frameNagusia, width=500, height=50)
        botoiakFrame.grid(row=0, column=1, pady=8)
        eguneratu = Button(botoiakFrame,text="Datuak eguneratu",command=lambda : self.datuakEguneratu())
        eguneratu.grid(row=0, column=0, padx=10)
        ekipamendua = Button(botoiakFrame,text="Ekipamenduak erakutsi",command=lambda : self.ekipamenduakErakutsi())
        ekipamendua.grid(row=0,column=2)
        bilaketaFrame = Frame(self.frameNagusia, width=500, height=150)
        bilaketaFrame.grid(row=1,column=1, pady=20)
        aukerakMota=["Guztiak","Kayaking","Run","Ride","Rowing"]
        aldagaiaMota = StringVar(bilaketaFrame)
        aldagaiaMota.set(aukerakMota[0])
        motak = OptionMenu(bilaketaFrame, aldagaiaMota, aukerakMota[0], *aukerakMota)
        motak.grid()
        noiztik = tk.Entry(bilaketaFrame, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        noiztik.grid()
        nora = tk.Entry(bilaketaFrame, textvariable=StringVar(value="Urtea-Hilabetea-Eguna"))
        nora.grid()
        bilatu = Button(bilaketaFrame,text="Bilatu",command=lambda : self.entrenamenduakBilatu(noiztik.get(), nora.get(), aldagaiaMota.get()))
        bilatu.grid()
        self.entrenamenduakIkusi() #Defektuz entrenamendu guztiak agertzeko
        self.window.mainloop()


    def datuakEguneratu(self):
        kudeatzaile.kargatuDB()
        tk.messagebox.showinfo(title="Datuak eguneratuta", message="Datuak ongi eguneratu dira!")

    def ekipamenduakErakutsi(self):
        EkipamenduLeihoa()

    def entrenamenduakIkusi(self):
        for frame in self.frames:
            frame.grid_forget()
            frame.destroy()
        self.frames.clear()
        entrenamenduak = kudeatzaile.entrenamenduakIkusi()
        col = 0
        r = 2
        for i in range(0,len(entrenamenduak)):
            if(col > 2):
                col = 0
                r = r + 1
            self.frames.append(tk.Frame(self.frameNagusia,relief=RAISED,bd=4))
            self.frames[i].grid(row=r,column=col,pady=20)
            #photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            #botoia=Button(frame, image = photo).pack()
            unekoEntrenamendua = entrenamenduak[i]
            izena = Button(self.frames[i],text=unekoEntrenamendua.izena,command=lambda i=i: self.entrenamenduaBistaratu(entrenamenduak[i]))
            izena.grid()
            data = Label(self.frames[i],text=f"Data: {unekoEntrenamendua.hasieraData}")
            data.grid()
            mota = Label(self.frames[i],text=f"Mota: {unekoEntrenamendua.mota}")
            mota.grid()
            distantzia = Label(self.frames[i],text=f"Distantzia: {unekoEntrenamendua.distantzia}m")
            distantzia.grid()
            denbora = Label(self.frames[i],text=f" Denbora: {unekoEntrenamendua.denbora} segundu")
            denbora.grid()
            col = col + 1

    def entrenamenduakBilatu(self,noiztik,nora,mota):
        for frame in self.frames:
            frame.grid_forget()
            frame.destroy()
        self.frames.clear()
        entrenamenduak = kudeatzaile.entrenamenduakBilatu(noiztik,nora,mota)
        col = 0
        r = 2
        for i in range(0,len(entrenamenduak)):
            if(col > 2):
                col = 0
                r = r + 1
            self.frames.append(tk.Frame(self.frameNagusia,relief=RAISED,bd=4))
            self.frames[i].grid(row=r,column=col,pady=20)
            #photo = tk.PhotoImage(file = f"{dirname}/irudiak/IMG_entrenamendua.png")
            #botoia=Button(frame, image = photo).pack()
            unekoEntrenamendua = entrenamenduak[i]
            izena = Button(self.frames[i],text=unekoEntrenamendua.izena,command=lambda i=i: self.entrenamenduaBistaratu(entrenamenduak[i]))
            izena.grid()
            data = Label(self.frames[i],text=f"Data: {unekoEntrenamendua.hasieraData}")
            data.grid()
            mota = Label(self.frames[i],text=f"Mota: {unekoEntrenamendua.mota}")
            mota.grid()
            distantzia = Label(self.frames[i],text=f"Distantzia: {unekoEntrenamendua.distantzia}m")
            distantzia.grid()
            denbora = Label(self.frames[i],text=f" Denbora: {unekoEntrenamendua.denbora} segundu")
            denbora.grid()
            col = col + 1
        

    def entrenamenduaBistaratu(self, entrenamendua):
        EntrenamenduLeihoa(entrenamendua)
