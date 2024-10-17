
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

class Register:
    
    def __init__(self, root):
        icon_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'icons', 'iconPass.ico')
        font_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'fonts', 'TechNoir-8dLD.ttf')
        ctypes.windll.gdi32.AddFontResourceW(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)

        customFontForSingUp = tkFont.Font(family="Tech Noir" , size=50)
        customFontSlogan = tkFont.Font(family="Tech Noir" , size=35)
        customFontRegister = tkFont.Font(family = "Tech Noir" , size=13)
        
        self.root = root
        #self.root.attributes("-fullscreen" , True)
        self.size = tk.Tk.geometry(self.root,"1200x700+660+300")
        self.resizable = tk.Tk.resizable(self.root, False , False)
        self.root.attributes('-topmost' , 0) 
        self.root.iconbitmap(icon_path)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("MainFrame.TFrame" , background = "#070A1C")
        style.configure("MainFrame2.TFrame" , background ="#0D112B")

        self.MainFrame = ttk.Frame(self.root , style="MainFrame.TFrame" , width=660 , height=700)
        self.MainFrame.pack(expand=True , fill="both" , side = LEFT)

        self.MainFrame2 = ttk.Frame(self.root , style="MainFrame2.TFrame" , width=560 , height=700)
        self.MainFrame2.pack(expand=True , fill="both" , side = RIGHT)

        self.SingUpMainFrame = ttk.Label(self.MainFrame, text="Sing" , font=customFontForSingUp , foreground="white" , background="#070A1C")
        self.SingUpMainFrame.place(x=50 , y=50)

        self.SingUpMainFrameSeconPart = ttk.Label(self.MainFrame, text="Up" , font=customFontForSingUp , foreground="#6CB8FF" , background="#070A1C")
        self.SingUpMainFrameSeconPart.place(x=244 , y=50)

        self.SloganMainFrame2 = ttk.Label(self.MainFrame2 ,  text="Your" , font=customFontSlogan , foreground="white" , background="#0D112B" )
        self.SloganMainFrame2.place(x=80  , y = 80)

        self.Slogan2MainFrame2 = ttk.Label(self.MainFrame2 ,  text="data" , font=customFontSlogan , foreground="#698CFF" , background="#0D112B" )
        self.Slogan2MainFrame2.place(x=260  , y = 80)

        self.Slogan3MainFrame2 = ttk.Label(self.MainFrame2 ,  text="," , font=customFontSlogan , foreground="white" , background="#0D112B" )
        self.Slogan3MainFrame2.place(x=420  , y = 80)

        self.Slogan4MainFrame2 = ttk.Label(self.MainFrame2 , text="Your" , font=customFontSlogan , foreground="white" , background="#0D112B" )
        self.Slogan4MainFrame2.place(x=136 , y=150)

        self.Slogan5MainFrame2 = ttk.Label(self.MainFrame2 , text="rules" , font=customFontSlogan , foreground="#698CFF" , background="#0D112B")
        self.Slogan5MainFrame2.place(x=310 , y=150)


        img1 = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/account-protection.png"   
        self.imageOpen1 = Image.open(img1).resize((500,500))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen1)

        self.lockSec = tk.Label(self.MainFrame2 , image=self.imageSecurty , bg="#0D112B")
        self.lockSec.place(x=50 , y=270)
        self.lockSec.image = self.imageSecurty #self.lockSec.image per fare riferimento all ogetto dell immagine quando ci troviamo in altre pagine di routing


        self.usernameText = ttk.Label(self.MainFrame , text="Username" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.usernameText.place(x=140, y=170)
        self.usernameSingUp = tk.Entry(self.MainFrame , width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.usernameSingUp.place(x=140, y=200 , height=35)


        self.passwordText = ttk.Label(self.MainFrame , text="Password" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.passwordText.place(x=140, y=250)
        self.passwordInput = tk.Entry(self.MainFrame ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.passwordInput.place(x=140, y=280 , height=35)


        self.emailText = ttk.Label(self.MainFrame , text="Email" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.emailText.place(x=140, y=330)
        self.emailInput = tk.Entry(self.MainFrame ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.emailInput.place(x=140, y=360 , height=35)


        self.nameText = ttk.Label(self.MainFrame , text="Name" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.nameText.place(x=140, y=410)
        self.nameTextInput = tk.Entry(self.MainFrame ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.nameTextInput.place(x=140, y=440 , height=35)


        self.phoneText = ttk.Label(self.MainFrame , text="Phone Number" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.phoneText.place(x=140, y=490)
        self.phoneTextInput = tk.Entry(self.MainFrame ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.phoneTextInput.place(x=140, y=520 , height=35)


        self.buttonRegister = tk.Button(self.MainFrame , text="Sing Up" , bg="#0787FF" , takefocus=0 , width=25 , height=3 , foreground="white" , font=customFontRegister , borderwidth=0)
        self.buttonRegister.place(x=140 , y=590)

        


