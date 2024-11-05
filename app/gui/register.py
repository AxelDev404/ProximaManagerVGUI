
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.font as tkFont 
from tkinter import PhotoImage
from tkinter import messagebox
import os
import sys
import ctypes
from PIL import Image, ImageTk  

from logic.User.db_user_manager import userManagement 
from logic.User.User import User


def resource_path(relative_path):

    try:
        # PyInstaller crea una cartella temporanea e memorizza il percorso in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Register:
    
    
    def __init__(self, root):
        icon_path = resource_path("assets/icons/iconPass.ico")
        font_path = resource_path("assets/fonts/TechNoir-8dLD.ttf")
        ctypes.windll.gdi32.AddFontResourceW(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)

        customFontForSingUp = tkFont.Font(family="Tech Noir" , size=50)
        customFontSlogan = tkFont.Font(family="Tech Noir" , size=35)
        customFontRegister = tkFont.Font(family = "Tech Noir" , size=13)
        
        self.root = root
        self.root.title("PROXIMA MANAGER")
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

        img1 = resource_path("assets/img/account-protection.png")
        self.imageOpen1 = Image.open(img1).resize((500,500))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen1)

        self.lockSec = tk.Label(self.MainFrame2 , image=self.imageSecurty , bg="#0D112B")
        self.lockSec.place(x=50 , y=270)
        self.lockSec.image = self.imageSecurty #self.lockSec.image per fare riferimento all ogetto dell immagine quando ci troviamo in altre pagine di routing


        self.inputVarUsername = tk.StringVar()
        self.inputVarPassword = tk.StringVar()
        self.inputVarEmail = tk.StringVar()
        self.inputVarName = tk.StringVar()
        self.inputVarPhone = tk.StringVar()

        self.inputVarUsername.set("")
        self.inputVarPassword.set("")
        self.inputVarEmail.set("")
        self.inputVarName.set("")
        self.inputVarPhone.set("")

        self.usernameText = ttk.Label(self.MainFrame , text="Username" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.usernameText.place(x=140, y=170)
        self.usernameSingUp = tk.Entry(self.MainFrame, textvariable=self.inputVarUsername , width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.usernameSingUp.place(x=140, y=200 , height=35)


        self.passwordText = ttk.Label(self.MainFrame , text="Password" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.passwordText.place(x=140, y=250)
        self.passwordInput = tk.Entry(self.MainFrame, textvariable=self.inputVarPassword ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.passwordInput.place(x=140, y=280 , height=35)


        self.emailText = ttk.Label(self.MainFrame , text="Email" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.emailText.place(x=140, y=330)
        self.emailInput = tk.Entry(self.MainFrame, textvariable=self.inputVarEmail ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.emailInput.place(x=140, y=360 , height=35)


        self.nameText = ttk.Label(self.MainFrame , text="Name" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.nameText.place(x=140, y=410)
        self.nameTextInput = tk.Entry(self.MainFrame, textvariable=self.inputVarName ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.nameTextInput.place(x=140, y=440 , height=35)


        self.phoneText = ttk.Label(self.MainFrame , text="Phone Number" , font="Helvetica 11 " , foreground="#0787FF" , background="#070A1C")
        self.phoneText.place(x=140, y=490)
        self.phoneTextInput = tk.Entry(self.MainFrame, textvariable=self.inputVarPhone ,  width=41 , font=("Arial" , 11) , takefocus=0 , borderwidth=1 ,bg="white" , foreground="black")
        self.phoneTextInput.place(x=140, y=520 , height=35)


        self.buttonRegister = tk.Button(self.MainFrame , text="Sign Up" , bg="#0787FF" , takefocus=0 , width=25 , height=3 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.signIn)
        self.buttonRegister.place(x=140 , y=590)

    
    def signIn(self):
        
        username = self.usernameSingUp.get().strip()
        password = self.passwordInput.get().strip()
        email = self.emailInput.get().strip()
        name = self.nameTextInput.get().strip()
        number_phone = self.phoneTextInput.get().strip()
        usrManger = userManagement()

        if not(username == "" or password == "" or email == "" or name == "" or number_phone == ""):

            if len(number_phone) == 10:
        
                usr = User(username , password , name , email , number_phone)
        
                if usrManger.checkExistanceUserinDb(username , email):
                    print("DEBUG : false")
                else:
                    from gui.main_window import MainWindow
                    usrManger.signIn(usr)

                    self.root.destroy()
                    goLogIn = tk.Tk()
                    quit =  MainWindow(goLogIn)
            else:
                messagebox.showerror("Proxima Message                                                             ","Number phone must be equal to 10 digits")
        else:
            messagebox.showerror("Proxima Message                                                             ","All the fields must be not empty")



