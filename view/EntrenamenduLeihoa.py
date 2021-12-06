import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.constants import RAISED
from view import ScrollContainer
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import os
import urllib.parse
import urllib3
from PIL import Image, ImageTk
import io
dirname = os.path.dirname(__file__)


class EntrenamenduLeihoa():
    def __init__(self,entrenamendua):
        self.window = tk.Toplevel()
        self.window.geometry('1500x800')
        self.window.title("Entrenamendua")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frameNagusia.grid_rowconfigure(1, weight=1)
        self.frameNagusia.grid_columnconfigure(1, weight=1)
        self.canvas = None
        self.entrenamenduaErakutsi(entrenamendua)
        self.bueltakErakutsi(entrenamendua)
        self.mapaErakutsi(entrenamendua)
        bilaketaFrame = Frame(self.frameNagusia, width=500, height=150)
        bilaketaFrame.grid(pady=6)
        aukerakX=["Denbora","Distantzia"]
        aldagaiaX = StringVar(bilaketaFrame)
        aldagaiaX.set(aukerakX[0])
        motakX = OptionMenu(bilaketaFrame, aldagaiaX, aukerakX[0], *aukerakX)
        motakX.grid()
        aukerakY=["Abiadura","Pultsazioa","Altitudea"]
        aldagaiaY = StringVar(bilaketaFrame)
        aldagaiaY.set(aukerakY[0])
        motakY = OptionMenu(bilaketaFrame, aldagaiaY, aukerakY[0], *aukerakY)
        motakY.grid()
        erakutsi = Button(bilaketaFrame,text="Grafikoa erakutsi",command=lambda : self.grafikoaErakutsi(entrenamendua, aldagaiaX.get(), aldagaiaY.get()))
        erakutsi.grid()
        self.grafikoaErakutsi(entrenamendua, "Denbora", "Abiadura")
        self.window.mainloop()

    def entrenamenduaErakutsi(self,entrenamendua):
        frameEntr= tk.Frame(self.frameNagusia)
        frameEntr.grid_rowconfigure(1, weight=1)
        frameEntr.grid_columnconfigure(1, weight=1)
        frameEntr.grid(pady=25)
        frameID = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameID.grid(row=1,column=0,sticky="ew")
        t1 = tk.Label(frameID,text="___________ID___________",bg="gray")
        id = tk.Label(frameID,text=entrenamendua.ID)
        t1.grid()
        id.grid()
        frameIkus = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameIkus.grid(row=1,column=1,sticky="ew")
        t2 = tk.Label(frameIkus,text="______Ikusgarritasuna______",bg="gray")
        ikusgarritasuna = tk.Label(frameIkus,text=entrenamendua.ikusgarritasuna)
        t2.grid()
        ikusgarritasuna.grid()
        frameIzena = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameIzena.grid(row=1,column=2,sticky="ew")
        t3 = tk.Label(frameIzena,text="_________Izena_________",bg="gray")
        izena = tk.Label(frameIzena,text=entrenamendua.izena)
        t3.grid()
        izena.grid()
        frameData = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameData.grid(row=1,column=3,sticky="ew")
        t4 = tk.Label(frameData,text="__________Data__________",bg="gray")
        data = tk.Label(frameData,text=entrenamendua.hasieraData)
        t4.grid()
        data.grid()
        frameMota = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameMota.grid(row=2,column=0,sticky="ew")
        t5 = tk.Label(frameMota,text="_________Mota__________",bg="gray")
        mota = tk.Label(frameMota,text=entrenamendua.mota)
        t5.grid()
        mota.grid()
        frameDis = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameDis.grid(row=2,column=1,sticky="ew")
        t6 = tk.Label(frameDis,text="________Distantzia_________",bg="gray")
        distantzia = tk.Label(frameDis,text=entrenamendua.distantzia)
        t6.grid()
        distantzia.grid()
        frameDenb = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameDenb.grid(row=2,column=2,sticky="ew")
        t7 = tk.Label(frameDenb,text="_______Denbora________",bg="gray")
        denbora = tk.Label(frameDenb,text=entrenamendua.denbora)
        t7.grid()
        denbora.grid()
        frameAbMax = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameAbMax.grid(row=2,column=3,sticky="ew")
        t8 = tk.Label(frameAbMax,text="______AbiaduraMax______",bg="gray")
        abiaduraMax = tk.Label(frameAbMax,text=entrenamendua.abiaduraMax)
        t8.grid()
        abiaduraMax.grid()
        frameAbBzb = tk.Frame(frameEntr,relief=RAISED,bd=3)
        frameAbBzb.grid(row=3,column=0,sticky="ew")
        t9 = tk.Label(frameAbBzb,text="______AbiaduraBzb______",bg="gray")
        abiaduraBzb = tk.Label(frameAbBzb,text=entrenamendua.abiaduraBzb)
        t9.grid()
        abiaduraBzb.grid()

    def grafikoaErakutsi(self,entrenamendua,xAld,yAld):
        if self.canvas != None:
            self.canvas.get_tk_widget().grid_forget()
        if xAld == "Denbora":
            xTmp = entrenamendua.streamDenborak.replace('[','')
            xTmp = xTmp.replace(']','')
            xTmp = xTmp.split(', ')
        elif xAld == "Distantzia":
            xTmp = entrenamendua.streamDistantziak.replace('[','')
            xTmp = xTmp.replace(']','')
            xTmp = xTmp.split(', ')
        if yAld == "Abiadura":
            yTmp = entrenamendua.streamAbiadurak.replace('[','')
            yTmp = yTmp.replace(']','')
            yTmp = yTmp.split(', ')
        elif yAld == "Pultsazioa":
            yTmp = entrenamendua.streamPultsazioak.replace('[','')
            yTmp = yTmp.replace(']','')
            yTmp = yTmp.split(', ')
        elif yAld == "Altitudea":
            yTmp = entrenamendua.streamAltitudeak.replace('[','')
            yTmp = yTmp.replace(']','')
            yTmp = yTmp.split(', ')
        x = []
        y = []
        sartu = True #Puntu gehiegi ez egoteko grafikoan (ez da ondo ikusten grafikoa puntu askorekin)
        for bal in xTmp:
            if(sartu):
                x.append(float(bal))
                sartu = False
            else:
                sartu = True

        sartu = True
        for bal in yTmp:
            if(sartu):
                y.append(float(bal))
                sartu = False
            else:
                sartu = True

        fig = Figure(figsize = (15,5),dpi=100)
        g = fig.add_subplot(111)
        g.plot(x,y)
        g.set_ylabel(yAld, fontsize=14)
        g.set_xlabel(xAld, fontsize=14)
        self.canvas = FigureCanvasTkAgg(fig,master = self.frameNagusia)  
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(pady=5)

    def bueltakErakutsi(self,entrenamendua):
        bueltak = kudeatzaile.entrenamenduarenBueltakIkusi(entrenamendua)
        datuak = []
        for buelta in bueltak:
            datuak.append((buelta.izena, buelta.distantzia, buelta.denbora, buelta.abiaduraBzb, buelta.pultsazioBzb))

        goiburuak = ["Izena", "Distantzia(m)", "Denbora(s)", "AbiaduraBzb(m/s)", "PultsazioaBzb"]
        taula = ttk.Treeview(self.frameNagusia, columns=(0,1,2,3,4), show='headings')

        for i,g in enumerate(goiburuak):
            taula.column(f"#{i}", minwidth=0, width=300)
            taula.heading(i, text=g)

        for i,d in enumerate(datuak):
            taula.insert(parent='', index=i, iid=i, values=d)
            
        taula.grid(pady=15)

    def mapaErakutsi(self,entrenamendua):
        token = "pk.eyJ1IjoiaWdvcmlzYXNpIiwiYSI6ImNrd3V4dGRncjFkaXIyb2xzODFjcWN1OGcifQ.izWu_zUPNQQw8eeqgCuKfg"
        strokeWidth = 1
        strokeColor = "f44"
        http = urllib3.PoolManager()
        polyline_ = urllib.parse.quote_plus(entrenamendua.mapa)
        path = f"path-{strokeWidth}+{strokeColor}({polyline_})"
        host = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
        tamaina = "/auto/1000x550"
        url = f"{host}{path}{tamaina}?access_token={token}"
        em = http.request('GET', url)
        # Irudiaren data irakurri eta argazkia sortu
        img = Image.open(io.BytesIO(em.data))
        # Tkinter en argazkia sortu
        # oso importantea self ekin gordetzea, bestela argazkia ezabatu egingo da.
        self.img2 = ImageTk.PhotoImage(img)
        # Label batean sartu
        panel = tk.Label(self.frameNagusia, image=self.img2)
        # bistaratu
        panel.grid(pady=25)
