
import tkinter as tk
from tkinter import font

class MainWindow:

    def __init__(self , root) :
        self.root  = root #test private after
        self.root.title("PROXIMA MANAGER")
        self.size = tk.Tk.geometry(self.root , "500x500") #secondary parameter is always sel.root to call main and execute 
        self.bgColor = tk.Tk.configure(self.root , background="#0B192C")

        #FONT DEFINE#
        font_style = font.Font(family="Helvetica" , size=12 , weight = "normal" )

        #MAIN WINDOWS
        self.setLabel = tk.Label(self.root, text="Sing in Proxima Manager" , font=font_style , background="#0B192C" , foreground="white").pack()
        self.setLabel2 = tk.Label(self.root , text="Username" , font=font_style , background="#0B192C" , foreground="white").pack(pady=20 , side="left")
        self.button1 = tk.Button(self.root , text="Sing in" , font=font_style, background="#7E60BF" , foreground="white" , width=30 ).pack(fill="x" , side="right" , padx="100")



    
    #def are the new function who manage the window like log in or error logIn authentification and all will be managed with the event listner with comand=self.on_button_clcik and de def will be execute it