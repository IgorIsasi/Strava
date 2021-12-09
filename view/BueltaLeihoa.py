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
        self.window.geometry('1150x700')
        self.window.title("Buelta")
        scroll = ScrollContainer(self.window)
        self.frameNagusia = scroll.second_frame
        self.frameNagusia.grid_rowconfigure(1, weight=1)
        self.frameNagusia.grid_columnconfigure(1, weight=1)
        self.canvas = None
        self.bueltaErakutsi(buelta)
        self.mapaErakutsi(entrenamendua,buelta)
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
        polyline_ = "mtfgGbicQCs%40Iy%40Ie%40%5DuAkAwCAGBMHGJ%40DBJPFxAHt%40z%40nDNXt%40v%40LV%3FRITIBGAECGOKc%40IgAkAcEOgAWmAk%40eDc%40uA%5D_AOYg%40o%40aCmB_%40a%40%5Be%40q%40kAk%40oA%7DBeG_%40s%40KMQKs%40MOGm%40e%40OIoAK%5DKYSQSS%5BMYKg%40E%5DKkBFsG%5BoBGiAB_GJcC%3FwCCaAKc%40Oa%40OWSSSOeAi%40m%40S_Bu%40g%40e%40Ue%40%5DkASeAI_AAs%40D%7B%40A%5BB%7BAC%7D%40Em%40Km%40e%40aBKw%40CCK%3FIN%3FLl%40rAT~%40Hl%40PbCD%7C%40Ad%40IzA%40bAFj%40ZtAVf%40TXVV%5CTd%40Nf%40HtAX~%40%60%40RPPXPh%40DVF~%40%3FbBSbSIxDBxAFlAHh%40Lh%40Pd%40Vf%40TT%5CTn%40R~APj%40Jr%40XVNTRb%40l%40l%40pAr%40bBn%40~Bl%40tAf%40r%40l%40r%40%5C%5EpAfA%60%40j%40d%40dA%5ErA%60%40rBZrBd%40xBHTLz%40x%40dDp%40zB%40ZGfABd%40FXFLHHH%40FK%40WKm%40Ou%40MiA%7B%40wC_BiGYkAu%40kEQy%40Yw%40%7B%40sAyAqAi%40s%40kBgE%7D%40aCiAaCe%40w%40SSQK%7BAk%40k%40KaAGk%40QYSWYMSSe%40Oo%40KcAEyCU%7DBE_ADyFTuH%40mCA%7D%40Ec%40Ia%40Qc%40U_%40%5B%5Bw%40e%40yBk%40e%40QSOQQ_%40s%40%5DkAGw%40AmBFuCMeBIo%40WeAi%40_BEGGAKJ%3FPd%40%60ARj%40XhAJr%40L%60BBbAIlB%3FdALlAVz%40%5El%40XRr%40R%60Cd%40z%40%5EXVV%5CLZJ%60%40Dl%40%40b%40GjHJ~B%40jAGlE%40~AArAGbBAxADv%40Nr%40d%40fAZb%40RNZLh%40HhBHz%40HXLZT%5Ed%40T%5CzBnFd%40tAb%40%60AxAdCdAtAlAjBd%40nB%60A%7CE%5ClAJV%5EfBd%40dBTvAJPJ%40DCDOGYwBmHw%40yCg%40aCs%40_CKW_A%7BAc%40k%40eAgAs%40iASc%40aAkCcAgCaAmBc%40m%40g%40%5By%40U_C%5D_%40KYOWS%5Dc%40Uc%40W%7B%40Sw%40Oy%40Eu%40AeADeIX%7DMAsBCk%40G%5BM_%40OYQSeBgAi%40SaASYMk%40g%40e%40%7D%40Qw%40I_AAiAF_EGiAOaAYiAc%40aBEGIAGL%40Tb%40fA%60%40tAJh%40NnADl%40%40hAGdC%3Fd%40F%7C%40R%7C%40LZT%5CTRZRl%40RpBb%40%60%40L%5ERTTRZPd%40Lh%40BX%40j%40EjEE~LInG%40lADdAJz%40Nn%40Pb%40T%60%40X%5CZV%5CLRDnBE%5EB%5CH%5CNTPRTd%40x%40t%40vA~%40jC~%40%60ChAjBfCfDl%40jAr%40rBlBbIvAzC%60%40pALl%40E%5E kmfgGrlcQf%40Mf%40APElAu%40pAq%40jAg%40%7C%40W%60%40Oj%40_%40vCoCZUXIn%40AjAFr%40%3Fp%40K%7C%40a%40dEoCxBcAr%40St%40E%5E%3FfC%5Cr%40BbBAv%40B%60Fv%40nA%5C%60%40DnAFx%40HlBd%40n%40Jd%40%40jAKn%40%40h%40Hl%40VZH~CLdBLl%40%3Ft%40MfA_%40hAs%40fCm%40XO%60%40U%60ByAjBiB%7CAqAhBgBbCsBz%40i%40z%40%5BrD_B%60Am%40pAaA~%40i%40b%40a%40bFsFfAgApAgB%7CFqJjAwAjAgB%60%40s%40~%40oCTgAPyBByACaBMcCOsB%5DmDo%40_Ki%40aFUgB_%40_BeA_EoA%7BDYyAKiAG_%40UgAa%40oAI_%40MeAM_%40Im%40a%40_Ba%40qBQk%40Iq%40Ic%40oBuH_AkEi%40mBm%40aBGg%40%40i%40GEAGCoASyCIgDDoFAc%40DoCEcAEUA%5D%3FcFP%7DCp%40aFTs%40FYLOPa%40%60BiEd%40w%40T%5BbAcAfAwAhBuBhBcCf%40i%40%40KGMQAUHWNa%40%5C%7BC~C_DzDgA~A%7B%40%60BcAzBk%40dBEVe%40jDGv%40M~CQjJAbC%40x%40%3FtDHpCTpC%5ClClA%7CHlDdOb%40bCj%40rC~%40jE%5ClAt%40bEpAfEt%40rC%5CnBjAtFh%40zChAhP%60%40lI%40vAGlBS%60Bg%40%7CAm%40tAiCxEyFrI_BlBsDxDkBhBuAlAkAz%40gC~AaCrA_BfAiBvAcFvEsAbAu%40d%40w%40b%40mB%60Aq%40XqBp%40k%40Nm%40JcALyAHqAByDEmG%5DmD%5D%7BDq%40uBg%40mCw%40qB%5B_%40CqA%3FkBJ_ANo%40PuAh%40kB%7C%40%7BBbBoFtEkBpAiBbAkB%7C%40_AZuIfC%5BH%5BB"
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
            #print(chunks[i]) #chunk-aren balio bitarra
            chunks[i] = int(chunks[i],2) #chunk-aren balioa hamartarrera pasatu
            if i < len(chunks)-1:
                chunks[i] = chunks[i] | 0x20 #balioari OR 0x20 egin azkenengo chunk-a ez bada
            chunks[i] = int(chunks[i]) + 63 #balioari 63 gehitu
            #print(chunks[i]) #chunk-aren balioa hamartarrean
            polyline = polyline + chr(int(chunks[i])) #chunk-en ASCII balioa string-ean sartu kateatuz
        #print(zenb, ": ", polyline)
        return polyline