import tkinter as tk
import tkinter.ttk as ttk
from controllers.DBKudeatzailea.DBKud import kudeatzaile


class EkipamenduLeihoa:
    def __init__(self):
        self.window = tk.Toplevel()
        leihoZabalera = 600
        leihoAltuera = 250
        x = (self.window.winfo_screenwidth() // 2) - (leihoZabalera // 2)
        y = (self.window.winfo_screenheight() // 2) - (leihoAltuera // 2)
        self.window.geometry('{}x{}+{}+{}'.format(leihoZabalera, leihoAltuera, x, y))
        self.window.title("Ekipamenduak")
        datuak = []
        ekipamenduak = kudeatzaile.ekipamenduenDistantziaIkusi()
        for ekipamendu in ekipamenduak:
            datuak.append((ekipamendu.izena,ekipamendu.marka,ekipamendu.modelo,ekipamendu.distantzia))

        goiburuak = ["Izena", "Marka", "Modeloa", "Distantzia"]
        taula = ttk.Treeview(self.window, columns=(0,1,2,3), show='headings')

        for i,g in enumerate(goiburuak):
            taula.column(f"#{i}", minwidth=0, width=100)
            taula.heading(i, text=g)

        for i,d in enumerate(datuak):
            taula.insert(parent='', index=i, iid=i, values=d)
            
        taula.pack()
        self.window.mainloop()