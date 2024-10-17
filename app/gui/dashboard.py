import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.font as tkFont 
from tkinter import PhotoImage
import ctypes
from PIL import Image, ImageTk  

class DashBoard:
    def __init__(self , root):
        self.root = root
        self.root  = root #test private after
        self.root.title("PROXIMA MANAGER")
        self.size = tk.Tk.geometry(self.root , "1920x1080+350+200")