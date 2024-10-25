
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

from logic.db_user_manager import userManagement


class DashBoard:
    def __init__(self , root , usernameLOGIN , passwordLOGIN):

        icon_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'icons', 'iconPass.ico')
        font_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'fonts', 'TechNoir-8dLD.ttf')

        ctypes.windll.gdi32.AddFontResourceW(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)

        customFontSingIn = tkFont.Font(family = "Tech Noir" , size=21)

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
        self.tab3 = tk.Frame(self.MainFrame , width=1500 , background = "#121528")
        self.tab4 = tk.Frame(self.MainFrame , width=1500 , background = "#121528")
        self.tab5 = tk.Frame(self.MainFrame , width=1500 , background = "#121528")

        self.labelTab1 = tk.Label(self.tab1, text="TEST TAB 1")
        self.labelTab2 = tk.Label(self.tab2, text="TEST TAB 2")
        self.labelTab3 = tk.Label(self.tab3, text="TEST TAB 3")
        self.labelTab4 = tk.Label(self.tab4, text="TEST TAB 4")
        self.labelTab5 = tk.Label(self.tab5, text="TEST TAB 5")
        

        self.labelTab1.pack()
        self.labelTab2.pack()
        self.labelTab3.pack()
        self.labelTab4.pack()
        self.labelTab5.pack()


        self.Title = tk.Label(self.MenuFrame , text="Proxima Manger" , font=customFontSingIn , background="#1B1A36" , foreground="white")
        self.Title.pack(fill="x" , pady=40)

        self.addCredentialsTab = tk.Button(self.MenuFrame , text="Add Credentials", font="Inter 13" , background="#1D2447", foreground="white", command=lambda: self.showTab(self.tab1) , border=0 , padx=5 , pady=5 , height=3 , cursor="hand2")
        self.addCredentialsTab.pack(fill="x" , pady=3)

        self.ViewAllCredentialsTab = tk.Button(self.MenuFrame , text="View all Credentials", font="Inter 13" , background="#1D2447", foreground="white" , command=lambda: self.showTab(self.tab2) , border=0 , padx=5 , pady=5 , height=3 , cursor="hand2")
        self.ViewAllCredentialsTab.pack(fill="x" , pady=3)

        self.FilterSearch = tk.Button(self.MenuFrame, text="Filter Search", font="Inter 13" , background="#1D2447", foreground="white" , command=lambda: self.showTab(self.tab3) , border=0 , padx=5 , pady=5 , height=3 , cursor="hand2")
        self.FilterSearch.pack(fill="x" , pady=3)

        self.ManageCredentials = tk.Button(self.MenuFrame , text="Manage Credentials" , font="Inter 13" , background="#1D2447", foreground="white" , command=lambda: self.showTab(self.tab4) , border=0 , padx=5 , pady=5 , height=3 , cursor="hand2")
        self.ManageCredentials.pack(fill="x" , pady=3)

        self.addCredentialsTab.bind("<Enter>" ,self.on_hover)
        self.addCredentialsTab.bind("<Leave>" ,self.leave_hover)
        
        self.ViewAllCredentialsTab.bind("<Enter>" ,self.on_hover2)
        self.ViewAllCredentialsTab.bind("<Leave>" ,self.leave_hover2)

        self.FilterSearch.bind("<Enter>" ,self.on_hover3)
        self.FilterSearch.bind("<Leave>" ,self.leave_hover3)

        self.ManageCredentials.bind("<Enter>" , self.on_hover4)
        self.ManageCredentials.bind("<Leave>" , self.leave_hover4)

        self.AreaPersonal = tk.Frame(self.MenuFrame , width=300 , background="#111735" , height=300)
        self.AreaPersonal.pack(fill="x", side="bottom" )

        img2 = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/logout.png"
        self.imageOpen2 = Image.open(img2).resize((42,42))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen2)
        self.label2 = self.imageSecurty

        self.buttonQuit = tk.Button(self.AreaPersonal , image=self.label2 , background="#111735" , border=0 , padx=5 , pady=5 , activebackground="#111735" , cursor="hand2" , command=self.logOut)
        self.buttonQuit.pack(side="left" , padx=10 , pady=10)

        usrManager = userManagement()

        self.userNameToShow=usrManager.getUsernameProfile(usernameLOGIN , passwordLOGIN)
        #ciao = "ciao"
        self.userNameProfile = tk.Label(self.AreaPersonal , text="@"+self.userNameToShow, font="Inter 12 bold" , foreground="white" , background="#111735" , padx=7 , pady=7)
        self.userNameProfile.pack(side="left")


        imgSettings = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/settings.png"
        self.imageOpen2 = Image.open(imgSettings).resize((40,40))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen2)
        self.labelSettings = self.imageSecurty

        self.buttonSettings = tk.Button(self.AreaPersonal , image=self.labelSettings , background="#111735" , border=0 , padx=5 , pady=5 , activebackground="#111735" ,  cursor="hand2" , command=lambda:self.showTab(self.tab5))
        self.buttonSettings.pack(side="right" , padx=13 , pady=10)

    
    def logOut(self):
        from gui.main_window import MainWindow #richiamo qui per evitare problemi di loop nel routing

        self.root.destroy()
        goLogIn = tk.Tk()
        quit =  MainWindow(goLogIn)


    def showTab(self, tab_frame):
        for Widget in self.MainFrame.winfo_children():
            Widget.pack_forget()
        
        tab_frame.pack(fill = "both" , expand = True)
    

    def on_hover(self, e):
        self.addCredentialsTab.config(background = "#121528")
    def leave_hover(self, e):
        self.addCredentialsTab.config(background = "#1D2447")
        

    def on_hover2(self, e):
        self.ViewAllCredentialsTab.config(background = "#121528")
    def leave_hover2(self, a):
        self.ViewAllCredentialsTab.config(background = "#1D2447")


    def on_hover3(self, e):
        self.FilterSearch.config(background = "#121528")
    def leave_hover3(self, a):
        self.FilterSearch.config(background = "#1D2447")


    def on_hover4(self, e):
        self.ManageCredentials.config(background = "#121528")
    def leave_hover4(self , e):
        self.ManageCredentials.config(background = "#1D2447")