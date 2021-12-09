import tkinter as tk
import tkinter.ttk as ttk
from controllers.DBKudeatzailea.DBKud import kudeatzaile


class EkipamenduLeihoa:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('600x250')
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