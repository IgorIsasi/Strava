import tkinter as tk
from tkinter import messagebox
from tkinter.constants import RAISED
from tkinter.ttk import *
from controllers.DBKudeatzailea.DBKud import kudeatzaile
import os
dirname = os.path.dirname(__file__)


class EkipamenduLeihoa:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry('400x400')
        self.window.title("Ekipamendua")