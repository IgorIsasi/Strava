import tkinter as tk
from tkinter import messagebox
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import datuakGorde

class Leihoa():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x500')
        self.window.title("Ongi etorri")
        self.testua=tk.Label(self.window,text="Alo")
        self.testua.pack()
        self.botoia=tk.Button(self.window,text="Botoia", command=self.datuakKargatu)
        self.botoia.pack()
        self.window.mainloop()

    def datuakKargatu(self):
        kudeatzaile.konektatu()
        datuakGorde.getActivities(kudeatzaile)
        tk.messagebox.showinfo(title="Datuak eguneratuta", message="Datuak ongi eguneratu dira!")
        

