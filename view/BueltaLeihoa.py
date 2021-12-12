import tkinter as tk
from tkinter.constants import RAISED
from view import ScrollContainer
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import urllib3
import io
from PIL import Image, ImageTk

class BueltaLeihoa():
    def __init__(self,entrenamendua,buelta):
        self.window = tk.Toplevel()
        leihoZabalera = 1150
        leihoAltuera = 850
        x = (self.window.winfo_screenwidth() // 2) - (leihoZabalera // 2)
        y = (self.window.winfo_screenheight() // 2) - (leihoAltuera // 2)
        self.window.geometry('{}x{}+{}+{}'.format(leihoZabalera, leihoAltuera, x, y))
        self.window.title("Buelta")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frameNagusia.grid_rowconfigure(1, weight=1)
        self.frameNagusia.grid_columnconfigure(1, weight=1)
        self.canvas = None
        self.bueltaErakutsi(buelta)
        #self.mapaErakutsi(entrenamendua,buelta)
        bilaketaFrame = tk.Frame(self.frameNagusia, width=500, height=150)
        bilaketaFrame.grid(pady=6)
        aukerakX=["Denbora","Distantzia"]
        aldagaiaX = tk.StringVar(bilaketaFrame)
        aldagaiaX.set(aukerakX[0])
        motakX = tk.OptionMenu(bilaketaFrame, aldagaiaX, *aukerakX)
        motakX.grid()
        aukerakY=["Abiadura","Pultsazioa","Altitudea"]
        aldagaiaY = tk.StringVar(bilaketaFrame)
        aldagaiaY.set(aukerakY[0])
        motakY = tk.OptionMenu(bilaketaFrame, aldagaiaY, *aukerakY)
        motakY.grid()
        erakutsi = tk.Button(bilaketaFrame,text="Grafikoa erakutsi",command=lambda : self.grafikoaErakutsi(entrenamendua, buelta, aldagaiaX.get(), aldagaiaY.get()))
        erakutsi.grid()
        self.grafikoaErakutsi(entrenamendua, buelta, "Denbora", "Abiadura")
        self.window.mainloop()


    def bueltaErakutsi(self, buelta):
        frameBu= tk.Frame(self.frameNagusia)
        frameBu.grid_rowconfigure(1, weight=1)
        frameBu.grid_columnconfigure(1, weight=1)
        frameBu.grid(pady=25)
        frameID = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameID.grid(row=1,column=0,sticky="ew")
        t1 = tk.Label(frameID,text="___________ID___________",bg="gray")
        id = tk.Label(frameID,text=buelta.ID)
        t1.grid()
        id.grid()
        frameIzena = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameIzena.grid(row=1,column=1,sticky="ew")
        t2 = tk.Label(frameIzena,text="__________Izena__________",bg="gray")
        izena = tk.Label(frameIzena,text=buelta.izena)
        t2.grid()
        izena.grid()
        frameData = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameData.grid(row=1,column=2,sticky="ew")
        t3 = tk.Label(frameData,text="__________Data__________",bg="gray")
        data = tk.Label(frameData,text=buelta.dataOrdua)
        t3.grid()
        data.grid()
        frameDis = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameDis.grid(row=1,column=3,sticky="ew")
        t4 = tk.Label(frameDis,text="________Distantzia_________",bg="gray")
        distantzia = tk.Label(frameDis,text=buelta.distantzia)
        t4.grid()
        distantzia.grid()
        frameDenb = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameDenb.grid(row=2,column=0,sticky="ew")
        t5 = tk.Label(frameDenb,text="________Denbora________",bg="gray")
        denbora = tk.Label(frameDenb,text=buelta.denbora)
        t5.grid()
        denbora.grid()
        frameAbMax = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameAbMax.grid(row=2,column=1,sticky="ew")
        t6 = tk.Label(frameAbMax,text="______AbiaduraMax_______",bg="gray")
        abiaduraMax = tk.Label(frameAbMax,text=buelta.abiaduraMax)
        t6.grid()
        abiaduraMax.grid()
        frameAbBzb = tk.Frame(frameBu,relief=RAISED,bd=3)
        frameAbBzb.grid(row=2,column=2,sticky="ew")
        t7 = tk.Label(frameAbBzb,text="______AbiaduraBzb_______",bg="gray")
        abiaduraBzb = tk.Label(frameAbBzb,text=buelta.abiaduraBzb)
        t7.grid()
        abiaduraBzb.grid()
        framePultsMax = tk.Frame(frameBu,relief=RAISED,bd=3)
        framePultsMax.grid(row=2,column=3,sticky="ew")
        t8 = tk.Label(framePultsMax,text="_______PultsazioMax_______",bg="gray")
        pultsazioMax = tk.Label(framePultsMax,text=buelta.pultsazioMax)
        t8.grid()
        pultsazioMax.grid()
        framePultsBzb = tk.Frame(frameBu,relief=RAISED,bd=3)
        framePultsBzb.grid(row=3,column=0,sticky="ew")
        t8 = tk.Label(framePultsBzb,text="______PultsazioBzb______",bg="gray")
        pultsazioBzb = tk.Label(framePultsBzb,text=buelta.pultsazioBzb)
        t8.grid()
        pultsazioBzb.grid()

    def grafikoaErakutsi(self,entrenamendua,buelta,xAld,yAld):
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
        for i in range(buelta.streamStartIndex,buelta.streamEndIndex):
            x.append(float(xTmp[i]))
        for i in range(buelta.streamStartIndex,buelta.streamEndIndex):
            y.append(float(yTmp[i]))

        fig = Figure(figsize = (12,5),dpi=100)
        g = fig.add_subplot(111)
        g.plot(x,y)
        g.set_ylabel(yAld, fontsize=14)
        g.set_xlabel(xAld, fontsize=14)
        self.canvas = FigureCanvasTkAgg(fig,master = self.frameNagusia)  
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(pady=5)

    def mapaErakutsi(self,entrenamendua,buelta):
        latLng = entrenamendua.streamLatLng.replace('[','')
        latLng = latLng.replace(']','')
        latLng = latLng.split(', ')
        koordenatuak = []
        for i in range(buelta.streamStartIndex * 2,(buelta.streamEndIndex + 1) * 2):
            koordenatuak.append(float(latLng[i]))
        polyline_ = self.posizioGeografikotikPolylinetara(koordenatuak)
        print("polyline",polyline_)
        token = "pk.eyJ1IjoiaWdvcmlzYXNpIiwiYSI6ImNrd3V4dGRncjFkaXIyb2xzODFjcWN1OGcifQ.izWu_zUPNQQw8eeqgCuKfg"
        strokeWidth = 1
        strokeColor = "f44"
        http = urllib3.PoolManager()
        path = f"path-{strokeWidth}+{strokeColor}({polyline_})"
        host = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
        tamaina = "/auto/1000x550"
        url = f"{host}{path}{tamaina}?access_token={token}"
        em = http.request('GET', url)
        print("em buelta:",em.data)
        # Irudiaren data irakurri eta argazkia sortu
        img = Image.open(io.BytesIO(em.data))
        # Tkinter en argazkia sortu
        # oso importantea self ekin gordetzea, bestela argazkia ezabatu egingo da.
        self.img2 = ImageTk.PhotoImage(img)
        # Label batean sartu
        panel = tk.Label(self.frameNagusia, image=self.img2)
        # bistaratu
        panel.grid(pady=25)

    def posizioGeografikotikPolylinetara(self,koordenatuak):
        polyline = ''
        lehenengoKoord = True #lehenengo koordenatuan ez da offset kalkulatu behar
        for i in range(len(koordenatuak)):
            if not(lehenengoKoord):
                koord = koordenatuak[i] - koordenatuak[i-2] #offset kalkulatu
            else:
                koord = koordenatuak[i]
            polyline = polyline + self.kodifikatu(koord)
            if i == 1: #i bikoitiak latitudeak izango dira eta bakoitiak longitudeak
                lehenengoKoord = False
        return polyline

    def kodifikatu(self,zenb):
        # 2. Birderkatu zenbakia bider 1e5 eta borobildu    
        balioa = round(zenb * 100000)
        
        # Kontuan izan, balio negatibo bat, biren osagarriaren metodoa # erabiliz kalkulatu behar dela. Balio binarioa ezeztuz
        # eta emaitzari bat gehituz.
        if zenb < 0:
            balioa = (1 << 32) + balioa
        else:
            if (balioa & (1 << (32 - 1))) != 0:
                balioa = balioa - (1 << 32)

        balioBitar=f"{balioa:016b}" #balioa bitarrera pasatu

        while len(balioBitar) < 32:
            balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu

        # 4. Mugitu bitak 1 ezkerrera
        maskara = 2 ** len(balioBitar) - 1
        balioBitar = format((int(balioBitar,2) << 1) & maskara,"b")

        while len(balioBitar) < 32:
            balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu (bitak mugitzean gerta daiteke zeroak desagertzea)
        
        # 5. Jatorrizko balioa negatiboa bada, # balio binario ezeztu:
        if zenb <0:
            balioBitar = format(int(balioBitar,2) ^ 0xFFFFFFFF,"b")

            while len(balioBitar) < 32:
                balioBitar = "0" + balioBitar #balio bitarrari hasierako zeroak gehitu (ezeztatzean desagertu daitezke)

        # 6. Hartu bit-ak bostnaka geratzen den zenbakia > 0x20 den bitartean
        balioBitarAldrebes = balioBitar[::-1] #bitak alderantzizko ordenean gorde chunk-ak beharrezko ordenean gordetzeko (eskuinetik ezkerrera)
        chunks = []
        sartu = True
        for i  in range(0,len(balioBitarAldrebes),5):
            if (int(balioBitarAldrebes[i:i+5]) > 0) | (sartu == True): #hasierako chunk hutsak sartu behar dira, amaierakoak ez (bitak aldrebes daude)
                chunks.append(balioBitarAldrebes[i:i+5])
                if int(balioBitarAldrebes[i:i+5]) > 0: #azkenengo chunk hutsak ez sartzeko
                    sartu = False

        polyline = ""
        for i in range (len(chunks)):
            chunks[i] = chunks[i][::-1] #chunk bakoitzaren biten ordena alderantziz jarri (lehendik alderantziz zeuden, orain orden egokian jarri)
            chunks[i] = int(chunks[i],2) #chunk-aren balioa hamartarrera pasatu
            if i < len(chunks)-1:
                chunks[i] = chunks[i] | 0x20 #balioari OR 0x20 egin azkenengo chunk-a ez bada
            chunks[i] = int(chunks[i]) + 63 #balioari 63 gehitu
            polyline = polyline + chr(int(chunks[i])) #chunk-en ASCII balioa string-ean sartu kateatuz
        return polyline