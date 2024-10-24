
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.font as tkFont 
from tkinter import PhotoImage
from tkinter import messagebox

import ctypes
from PIL import Image, ImageTk  

import os

class DashBoard:
    def __init__(self , root):

        icon_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'icons', 'iconPass.ico')

        self.root = root
        self.root  = root #test private after
        self.root.title("PROXIMA MANAGER")
        self.size = tk.Tk.geometry(self.root , "1700x800+350+200")
        #self.resizable = tk.Tk.resizable(self.root, False , False)
        self.root.attributes('-topmost' , 0) 
        self.root.iconbitmap(icon_path)
        #self.root.configure(background = "#121528")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("MenuFarme.TFrame" , background = "#1B1A36")
        style.configure("MainFrame.TFrame" , background = "#121528")

        
        self.MenuFrame = ttk.Frame(self.root , style="MenuFarme.TFrame" , width=300 , height=700)
        self.MenuFrame.pack(fill="y" , side=LEFT)
        self.MenuFrame.pack_propagate(False) # blocco estensione del menu

        self.MainFrame = ttk.Frame(self.root , style="MainFrame.TFrame" , width=1500 , height=700)
        self.MainFrame.pack(fill=BOTH , expand=True , side=LEFT)

        self.tab1 = tk.Frame(self.MainFrame , width=1500 , background = "#121528")
        self.tab2 = tk.Frame(self.MainFrame , width=1500 , background = "#121528")

        self.labelTab1 = tk.Label(self.tab1, text="TEST TAB 1")
        self.labelTab2 = tk.Label(self.tab2, text="TEST TAB 2")

        self.labelTab1.pack()
        self.labelTab2.pack()

        self.addCredentialsTab = tk.Button(self.MenuFrame , text="Add Credentials", font="Inter 13" , background="#1D2447", foreground="white", command=lambda: self.showTab(self.tab1) , border=0 , padx=3 , pady=3)
        self.addCredentialsTab.pack(fill="x" , pady=2)

        self.ViewAllCredentialsTab = tk.Button(self.MenuFrame , text="View all Credentials", font="Inter 13" , background="#1D2447", foreground="white" , command=lambda: self.showTab(self.tab2) , border=0 , padx=3 , pady=3)
        self.ViewAllCredentialsTab.pack(fill="x" , pady=2)

        self.addCredentialsTab.bind("<Enter>" ,self.on_hover)
        self.addCredentialsTab.bind("<Leave>" ,self.leave_hover)

    
    def showTab(self, tab_frame):
        for Widget in self.MainFrame.winfo_children():
            Widget.pack_forget()
        
        tab_frame.pack(fill = "both" , expand = True)
    

    def on_hover(self, e):
        self.addCredentialsTab.config(background = "#121528")

    def leave_hover(self, e):
        self.addCredentialsTab.config(background = "#1D2447")