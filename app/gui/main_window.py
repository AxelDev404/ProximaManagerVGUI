
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

from gui.dashboard import DashBoard
from gui.register import Register

from logic.db_user_manager import userManagement

class MainWindow:

    def __init__(self , root) :

        icon_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'icons', 'iconPass.ico')
        img_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'img', 'account-protection.png')
        font_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'fonts', 'TechNoir-8dLD.ttf')

        ctypes.windll.gdi32.AddFontResourceW(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)
        

        self.root  = root #test private after
        self.root.title("PROXIMA MANAGER")
        self.size = tk.Tk.geometry(self.root , "1000x600+750+300") #secondary parameter is always self.root to call main and execute 
        self.resize= tk.Tk.resizable(self.root, False,False) #false 1 block reizable x 2 false resizable y
        self.root.attributes('-topmost' , 0) #sovrapposizione delle fiestre mettendo in secondo piano se seleziono altro
        self.root.iconbitmap(icon_path)

        customFontTitle1 = tkFont.Font(family = "Tech Noir" ,size=36)
        customFontTitle2 = tkFont.Font(family = "Tech Noir" , size=24)
        customFontRegister = tkFont.Font(family = "Tech Noir" , size=14)
        customFontSingIn = tkFont.Font(family = "Tech Noir" , size=21)
        
        #print(tkFont.families())

        style = ttk.Style()#per creare un stile da una classe=
        style.theme_use("clam")

        style.configure("MainFrame.TFrame", background="#070A1C")# Colore per il primo frame
        style.configure("MainFrame2.TFrame", background="#050617")  
        #style.configure("TButton", background="#0787FF" , relief="flat" , foreground = "white" , borderwidth = 0 , height=70)

        self.MainFrame2 = ttk.Frame(self.root , style="MainFrame2.TFrame", height=300 , width=400 )
        self.MainFrame2.pack(side=LEFT , fill="both", expand=True)
    
        self.MainFrame = ttk.Frame(self.root ,style="MainFrame.TFrame" , height=600 , width=750)
        self.MainFrame.pack(side=RIGHT , fill="both", expand=True)

        self.titleMainFrame2 = ttk.Label(self.MainFrame2 , text="Proxima" , font=customFontTitle1, background="#050617" , foreground="#4788FF")
        self.titleMainFrame2.place(x=50 , y=50)

        self.secondaryTitleMainFrame2 = ttk.Label(self.MainFrame2 , text="Manager" , font=customFontTitle2 , background="#050617" , foreground="white")
        self.secondaryTitleMainFrame2.place(x=130 , y= 100)

        img2 = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/account-protection.png"
        self.imageOpen2 = Image.open(img2).resize((240,240))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen2)

        self.label2 = tk.Label(self.MainFrame2 , image=self.imageSecurty , bg="#050617")
        self.label2.place(x=70 , y= 240)
        self.label2 = self.imageSecurty

        self.SingInMainFrame = ttk.Label(self.MainFrame , text="Sign In", background="#070A1C" , font=customFontSingIn , foreground="white")
        self.SingInMainFrame.place(x=100 , y=150)
        
        self.buttonRegister = tk.Button(self.MainFrame , text="Sign Up" , bg="#0787FF" , takefocus=0 , width=16 , height=3 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.registerPage , cursor="hand2")
        self.buttonRegister.place(x=100 , y=350)


        img = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/login-.png"
        self.imageOpen = Image.open(img).resize((50,50))
        self.ImageUp = ImageTk.PhotoImage(self.imageOpen)
        #self.label = tk.Label(self.MainFrame , image=self.ImageUp , bg="#0787FF")
        self.label = self.ImageUp

        self.buttonLogIn = tk.Button(self.MainFrame , text="LogIn", image=self.ImageUp , bg="#064988" , takefocus=0 , width=80 , height=62 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.logged , cursor="hand2")
        self.buttonLogIn.place(x=348 , y=350)

        self.inputVarUsername = tk.StringVar()
        self.inputVarPassword = tk.StringVar()

        self.inputVarUsername.set("")
        self.inputVarPassword.set("")
        
        self.username = ttk.Label(self.MainFrame , text="Username" , font="Helvetica 11 " , foreground="#4788FF" , background="#070A1C")
        self.username.place(x=97 , y=200)
        self.usernameInput = tk.Entry(self.MainFrame , width=41 , font=("Inter" , 11) , takefocus=0 , borderwidth=1 , textvariable=self.inputVarUsername)
        self.usernameInput.place(x=100 , y=225 , height=35)

        self.password = ttk.Label(self.MainFrame , text="Password" , font="Helvetica 11 " , foreground="#4788FF" , background="#070A1C")
        self.password.place(x=97 , y=270)
        self.passwordInput = tk.Entry(self.MainFrame , width=41 , font=("Inter" , 11) , takefocus=0 , show="•" , borderwidth=1 , textvariable=self.inputVarPassword)
        self.passwordInput.place(x=100 , y=293 , height=35)



    def logged(self):

        userManager = userManagement()
        
        username = self.usernameInput.get()
        password = self.passwordInput.get()

        if  userManager.logIn(username , password):
            self.root.destroy()
            dashRoot = tk.Tk()
            dash = DashBoard(dashRoot , username , password)
        else:
            messagebox.showerror("        Invalid credentials try again                                                         .")

            self.inputVarUsername.set("")
            self.inputVarPassword.set("")

    def registerPage(self):
        self.root.destroy()
        registerSectionRoot = tk.Tk()
        registrationSection = Register(registerSectionRoot)

        




    #self.btm = ttk.Button(self.MainFrame , text="dio cane")
          
    #def are the new function who manage the window like log in or error logIn authentification and all will be managed with the event listner with comand=self.on_button_clcik and de def will be execute it