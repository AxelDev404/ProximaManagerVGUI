
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

import mysql.connector 
from mysql.connector import Error

from logic.User.db_user_manager import userManagement
from logic.Credentials.db_credentials_manager import credentialsManagement
from logic.Credentials.Credentials import Credential



class DashBoard:
    def __init__(self , root , usernameLOGIN , passwordLOGIN):

        icon_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'icons', 'iconPass.ico')
        font_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'WorkSpace', 'WorkSpace', 'Python_projects', 'ProximaManagerVGUI', 'assets' , 'fonts', 'TechNoir-8dLD.ttf')

        ctypes.windll.gdi32.AddFontResourceW(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)

        customFontSingIn = tkFont.Font(family = "Tech Noir" , size=21)
        customFontRegister = tkFont.Font(family = "Tech Noir" , size=14)

        #CONSTRUCTORS

        usrManager = userManagement()
        crdManager = credentialsManagement()

        self.root = root
        self.root  = root #test private after
        self.root.title("PROXIMA MANAGER")
        self.size = tk.Tk.geometry(self.root , "1300x700+350+200")
        #self.resizable = tk.Tk.resizable(self.root, False , False)
        self.root.attributes('-topmost' , 0) 
        self.root.iconbitmap(icon_path)

        self.root.grid_columnconfigure(1, weight=1)  # Colonna 1 (contenuto) si espande
        self.root.grid_rowconfigure(0, weight=1)     # Riga 0 si espande verticalmente

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("MenuFarme.TFrame" , background = "#1B1A36")
        style.configure("MainFrame.TFrame" , background = "#121528")
        style.configure("mystyle.Treeview.Heading" , font=("Inter" , 10) , background = "#1D2447" , foreground="white" , fieldbackground="lightgray")

        self.MenuFrame = ttk.Frame(self.root , style="MenuFarme.TFrame" , width=300 , height=700)
        self.MenuFrame.grid(row=0, column=0, sticky="ns")
        self.MenuFrame.grid_propagate(False)       

        self.MainFrame = ttk.Frame(self.root , style="MainFrame.TFrame" , width=1500 , height=700)
        self.MainFrame.grid(row=0, column=1, sticky="nsew")
        self.MainFrame.grid_columnconfigure(0, weight=1)
        self.MainFrame.grid_rowconfigure(0, weight=1)

        self.tab1 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")

        self.tab2 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")

        self.tab2 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")

        self.tab3 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")
        self.tab4 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")
        self.tab5 = tk.Frame(self.MainFrame , width=1500 , bg = "#121528")

        for tab in [self.tab1]:
            tab.grid_rowconfigure(0, weight=0)  # Permette l'espansione della colonna
            tab.grid_rowconfigure(1, weight=0) #tolgo l espansione con lo 0   
            tab.grid_rowconfigure(2, weight=0) 
            tab.grid_rowconfigure(3, weight=0) #tolgo l espansione con lo 0   
            tab.grid_rowconfigure(4, weight=0) 
            tab.grid_rowconfigure(5, weight=0) #tolgo l espansione con lo 0   
            tab.grid_rowconfigure(6, weight=0) 
            tab.grid_rowconfigure(7, weight=0) #tolgo l espansione con lo 0   
            tab.grid_rowconfigure(8, weight=0) 
            tab.grid_rowconfigure(9, weight=0) 
            
            tab.grid_columnconfigure(0, weight=1)  # Permette l'espansione della colonna
            tab.grid_columnconfigure(1, weight=0)   
            tab.grid_columnconfigure(2, weight=1)  
            tab.grid_columnconfigure(3, weight=1)   
            tab.grid_columnconfigure(4, weight=1)  

        self.tab2.grid_rowconfigure(0,weight=1)
        self.tab2.grid_rowconfigure(1,weight=1)
        self.tab2.grid_columnconfigure(0,weight=1)

        self.tab3.grid_rowconfigure(0,weight=1)
        self.tab3.grid_rowconfigure(1,weight=1)
        self.tab3.grid_columnconfigure(0,weight=1)

        self.tab4.grid_rowconfigure(0,weight=0)
        self.tab4.grid_rowconfigure(1,weight=0)
        self.tab4.grid_rowconfigure(2,weight=0)
        self.tab4.grid_rowconfigure(3,weight=0)
        self.tab4.grid_rowconfigure(4,weight=0)
        self.tab4.grid_rowconfigure(5,weight=0)
        self.tab4.grid_rowconfigure(6,weight=0)
        self.tab4.grid_rowconfigure(7,weight=0)
        self.tab4.grid_rowconfigure(8,weight=0)
        self.tab4.grid_rowconfigure(9,weight=0)
        self.tab4.grid_rowconfigure(10,weight=0)
        self.tab4.grid_rowconfigure(11,weight=0)
        self.tab4.grid_rowconfigure(12,weight=0)
        self.tab4.grid_rowconfigure(13, weight=0)
        #self.tab4.grid_rowconfigure(14, weight=0)
        self.tab4.grid_columnconfigure(0,weight=1)


        self.tab5.grid_rowconfigure(0,weight=0)
        self.tab5.grid_rowconfigure(1,weight=0)
        self.tab5.grid_rowconfigure(2,weight=0)
        self.tab5.grid_rowconfigure(3,weight=0)
        self.tab5.grid_rowconfigure(4,weight=0)
        self.tab5.grid_rowconfigure(5,weight=0)
        self.tab5.grid_rowconfigure(6,weight=0)
        self.tab5.grid_rowconfigure(7,weight=0)
        self.tab5.grid_rowconfigure(8,weight=0)
        self.tab5.grid_rowconfigure(9,weight=0)
        self.tab5.grid_rowconfigure(10,weight=0)
        self.tab5.grid_rowconfigure(11,weight=0)
        self.tab5.grid_rowconfigure(12,weight=0)
        self.tab5.grid_rowconfigure(13, weight=0)
        #self.tab4.grid_rowconfigure(14, weight=0)

        self.tab5.grid_columnconfigure(0,weight=1)

        

        self.labelTab5 = tk.Label(self.tab5, text="TEST TAB 5")


        #ADD CREDENTIAL TAB#

        # Inizializza le StringVar
        self.inputVarUsername = tk.StringVar()
        self.inputVarPassword = tk.StringVar()
        self.inputVarEmail = tk.StringVar()
        self.inputVarProduct = tk.StringVar()

        # Imposta i valori iniziali (opzionale)
        self.inputVarUsername.set("")
        self.inputVarPassword.set("")
        self.inputVarEmail.set("")
        self.inputVarProduct.set("")


        self.Title =tk.Label(self.tab1 , text="Add Credentials" , font="Inter 13" , foreground="white" , background="#121528") 
        self.Title.grid(row = 0 , column=2, columnspan=2 , sticky="n" , pady=80)

        self.usernameTitle = tk.Label(self.tab1 , text="Username" , font="Inter 10" ,  foreground="white" , background="#121528")
        self.usernameTitle.grid(row=1 , column=2 , columnspan=2)

        self.usernameRegistration = tk.Entry(self.tab1, textvariable=self.inputVarUsername , width=42 , border=1 , bg="white" , foreground="black" , font=("Inter" , 11))
        self.usernameRegistration.grid(row=2 , column=2 ,  columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.passwordTitle =  tk.Label(self.tab1 , text="Password" , font="Inter 10" , foreground="white" , background="#121528")
        self.passwordTitle.grid(row=3 , column=2 , columnspan=2)

        self.passwordRegistration = tk.Entry(self.tab1, textvariable=self.inputVarPassword , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.passwordRegistration.grid(row=4 , column=2 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.emailTitle = tk.Label(self.tab1 ,  text="Email" , font="Inter 10" , foreground="white" , background="#121528")
        self.emailTitle.grid(row=5 , column=2 ,  columnspan=2)

        self.emailRegistration = tk.Entry(self.tab1, textvariable=self.inputVarEmail , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.emailRegistration.grid(row = 6 , column=2 ,  columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.productTitle = tk.Label(self.tab1 ,  text="Service" , font="Inter 10" , foreground="white" , background="#121528")
        self.productTitle.grid(row = 7 , column=2 ,  columnspan=2)

        self.productRegistration = tk.Entry(self.tab1, textvariable=self.inputVarProduct , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.productRegistration.grid(row = 8 , column=2 , columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.buttonAdd = tk.Button(self.tab1 , text="Add Credential" , bg="#3D4985" , takefocus=0 , width=26 , height=2 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.addCredential)
        self.buttonAdd.grid(row=9 , column=2 , columnspan=2 , pady=(20,0))



        #VIEW ALL CREDENTIALS TAB#
        style.configure("Treeview", 
                background="#131832", #black
                foreground="#0095FF", #green  RETRO STYLE
                fieldbackground="#131832", #black
                rowheight=25,
                font = ("Inter" , 10)
                )
        style.map("Treeview", background=[("selected", "#3D4985")])

        self.tree = ttk.Treeview(self.tab2 ,style="Treeview", column=("ID" , "USERNAME" , "PASSWORD" , "EMAIL" , "SERVICE") , show='headings')
        
        
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1" , text="ID" )
        self.tree.column("#2" , anchor=tk.CENTER)
        self.tree.heading("#2" , text="USERNAME")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3" , text="PASSWORD")
        self.tree.column("#4" , anchor=tk.CENTER)
        self.tree.heading("#4" , text="EMAIL")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5" , text="SERVICE")

        self.tree.grid(row=0 , column=0 , sticky="nsew" , pady=(30,0) , padx=(20,0))
        self.sby = ttk.Scrollbar(self.tab2 , orient=tk.VERTICAL , command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.sby.set)
        self.sby.grid(row = 0, column=1, sticky="ns" ,padx=(0,20) , pady=(30,0))

        self.idUser = usrManager.getIdUser(usernameLOGIN , passwordLOGIN)
        

        row2 = crdManager.viewAllCredentials(self.idUser)
        

        if row2 is None:
            print("DEBUG : no credentials founed for this user")
        else:
            for row in row2:
                idCredential = row[0] #predno la riga degli ID
                self.tree.insert("",tk.END ,iid=idCredential , values=row)
                self.tree.update_idletasks()

        for item in self.tree.get_children():
            print(" - iid:", item)



       #FILTER SEARCH TAB

        self.EntryFilterSearch = tk.Entry(self.tab3 , width=34 , font=("Inter" , 10) , background="white" , foreground="black")
        self.EntryFilterSearch.grid(row=1 , column=0 , sticky="n" , pady=(100,0) , ipadx=40, ipady=7)

        self.optionVariable = StringVar()
        self.optionVariable.set("Filters")

        self.optionList = ['ID CREDENTIAL' , 'USERNAME' , 'EMAIL' , 'SERVICE']


        self.openMenuChoose = tk.OptionMenu(self.tab3 , self.optionVariable , * self.optionList)
        self.openMenuChoose.config(border=0,  highlightthickness=0 , bg="#3D4985" ,  foreground="white" , font="Inter 11")
        self.openMenuChoose.grid(row=1 , column=0, sticky="n" ,padx=(0,500), pady=(99,0) , ipady=5)

        imgSearch = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/magnifying-glass.png"
        self.imageOpen2 = Image.open(imgSearch).resize((30,30))
        self.imageSerch = ImageTk.PhotoImage(self.imageOpen2)
        self.labelSearch = self.imageSerch

        self.buttonSearch= tk.Button(self.tab3 , image=self.labelSearch , background="#121528" , border=0 , padx=5 , pady=5 , activebackground="#121528" , cursor="hand2" , command=self.startSeacrch)
        self.buttonSearch.grid(row=1 , column=0 , sticky="n", pady=(101,0), padx=(380,0) )

        

        self.tree2 = ttk.Treeview(self.tab3 , column=("ID" , "USERNAME" , "PASSWORD" , "EMAIL" , "SERVICE") , show='headings')
        
        self.tree2.column("#1", anchor=tk.CENTER)
        self.tree2.heading("#1" , text="ID")
        self.tree2.column("#2" , anchor=tk.CENTER)
        self.tree2.heading("#2" , text="USERNAME")
        self.tree2.column("#3", anchor=tk.CENTER)
        self.tree2.heading("#3" , text="PASSWORD")
        self.tree2.column("#4" , anchor=tk.CENTER)
        self.tree2.heading("#4" , text="EMAIL")
        self.tree2.column("#5", anchor=tk.CENTER)
        self.tree2.heading("#5" , text="SERVICE")

        self.tree2.grid(row=0 , column=0 , sticky="nsew" , pady=(30,0) , padx=(20,0))
        self.sby2 = ttk.Scrollbar(self.tab3 , orient=tk.VERTICAL , command=self.tree2.yview)
        self.tree2.configure(yscrollcommand=self.sby2.set)
        self.sby2.grid(row = 0, column=1, sticky="ns" ,padx=(0,20) , pady=(30,0))


        #MANAGE CREDENTIALS TAB 


        self.inputIDVar = tk.IntVar()
        self.inputUsernameUpdate = tk.StringVar()
        self.inputPasswordUpdate = tk.StringVar()
        self.inputEmailUpdate = tk.StringVar()
        self.inputProductUpdate = tk.StringVar()

        self.inputIDVar.set(0)
        self.inputUsernameUpdate.set("")
        self.inputPasswordUpdate.set("")
        self.inputEmailUpdate.set("")
        self.inputProductUpdate.set("")

        self.manageVar = StringVar()
        self.manageVar.set("Filters")

        self.manageList = ['USERNAME', 'PASSWORD' , 'EMAIL' , 'SERVICE' , 'CHANGE ALL']

        self.Instruction = ttk.Label(self.tab4 , text="You have to select the filter to choose what you want to change in your credential clicking on the filters menu near ID input, after that you have to write the ID of your credential before to do any changes" , font="Inter 13" , foreground="white" , background="#121528")
        self.Instruction.grid(row = 1 , column=0 , pady=(80,30))

        self.modifyTarget = tk.OptionMenu(self.tab4 , self.manageVar , * self.manageList)
        self.modifyTarget.config(bg="#3D4985" ,  foreground="white" , font="Inter 11" , border=0 ,  highlightthickness=0)
        self.modifyTarget.grid(row=3 , column=0, columnspan=2 , pady=(0,10) ,ipady=5 , padx=(560,0))
        
        self.IdTitle = tk.Label(self.tab4 , text="ID" , font="Inter 10" ,  foreground="white" , background="#121528")
        self.IdTitle.grid(row=2 , column=0 , columnspan=2 , pady=(10,0))

        self.IdInput = tk.Entry(self.tab4, textvariable=self.inputIDVar , width=42 , border=1 , bg="#3D4985" , foreground="white" , font=("Inter" , 11))
        self.IdInput.grid(row=3 , column=0 ,  columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.pwdTitle =  tk.Label(self.tab4 , text="Password" , font="Inter 10" , foreground="white" , background="#121528")
        self.pwdTitle.grid(row=6 , column=0 , columnspan=2)

        self.pwdChange = tk.Entry(self.tab4, textvariable=self.inputPasswordUpdate , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.pwdChange.grid(row=7 , column=0 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.emailTitle2 = tk.Label(self.tab4 ,  text="Email" , font="Inter 10" , foreground="white" , background="#121528")
        self.emailTitle2.grid(row=8 , column=0 ,  columnspan=2 )

        self.emailChange = tk.Entry(self.tab4, textvariable=self.inputEmailUpdate , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.emailChange.grid(row=9 , column=0 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.usernameTitle2 = tk.Label(self.tab4 ,  text="Username" , font="Inter 10" , foreground="white" , background="#121528")
        self.usernameTitle2.grid(row=4 , column=0 ,  columnspan=2 )

        self.usernameChange = tk.Entry(self.tab4, textvariable=self.inputUsernameUpdate , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.usernameChange.grid(row=5 , column=0 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.productTitle = tk.Label(self.tab4 ,  text="Service" , font="Inter 10" , foreground="white" , background="#121528")
        self.productTitle.grid(row=10 , column=0 ,  columnspan=2 )

        self.productChange = tk.Entry(self.tab4, textvariable=self.inputProductUpdate , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.productChange.grid(row=11 , column=0 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.buttonAdd = tk.Button(self.tab4 , text="Update credential" , bg="#3D4985" , takefocus=0 , width=26 , height=2 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.changeUsernameCredential)
        self.buttonAdd.grid(row=12 , column=0 , columnspan=2 , pady=(20,10))

        self.buttonDel = tk.Button(self.tab4 , text="Delete credential" , bg="#3D4985" , takefocus=0 , width=26 , height=2 , foreground="white" , font=customFontRegister , borderwidth=0 ,  command=self.deleteCredential)
        self.buttonDel.grid(row=13 , column=0 , columnspan=2 , pady=(20,10))




        #PROFILE SETTINGS

        self.usernameProfile = tk.StringVar()
        self.passwordProfile = tk.StringVar()
        self.emailProfile = tk.StringVar()

        self.usernameProfile.set("")
        self.passwordProfile.set("")
        self.emailProfile.set("")

        self.Title = ttk.Label(self.tab5 , text="PROFILE SETTINGS" , font="Inter 13" , foreground="white" , background="#121528")
        self.Title.grid(row = 0 , column=0 , pady=(80,30))

        self.manageVarSettings = StringVar()
        self.manageVarSettings.set("Filters")

        self.manageListSettings = ['USERNAME', 'PASSWORD' , 'EMAIL']

        self.modifyTargetSetting = tk.OptionMenu(self.tab5 , self.manageVarSettings , * self.manageListSettings)
        self.modifyTargetSetting.config(bg="#3D4985" ,  foreground="white" , font="Inter 11" , border=0 ,  highlightthickness=0)
        self.modifyTargetSetting.grid(row=2 , column=0, columnspan=2 , pady=(0,10) ,ipady=5 , padx=(560,0))

        self.usernameTitleSetting = tk.Label(self.tab5 , text="Username" , font="Inter 10" ,  foreground="white" , background="#121528")
        self.usernameTitleSetting.grid(row=1 , column=0 , columnspan=2)

        self.usernameSetting = tk.Entry(self.tab5, textvariable=self.usernameProfile , width=42 , border=1 , bg="white" , foreground="black" , font=("Inter" , 11))
        self.usernameSetting.grid(row=2 , column=0 ,  columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.passwordTitleSetting =  tk.Label(self.tab5 , text="Password" , font="Inter 10" , foreground="white" , background="#121528")
        self.passwordTitleSetting.grid(row=3 , column=0 , columnspan=2)

        self.passwordSetting = tk.Entry(self.tab5, textvariable=self.passwordProfile , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.passwordSetting.grid(row=4 , column=0 , columnspan=2, pady=(0,10), ipadx=30, ipady=7)

        self.emailTitleSetting = tk.Label(self.tab5 ,  text="Email" , font="Inter 10" , foreground="white" , background="#121528")
        self.emailTitleSetting.grid(row=5 , column=0 ,  columnspan=2 )

        self.emailSetting = tk.Entry(self.tab5, textvariable=self.emailProfile , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.emailSetting.grid(row = 6 , column=0 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.buttonChangeProfile= tk.Button(self.tab5 , text="Update profile" , bg="#3D4985" , takefocus=0 , width=26 , height=2 , foreground="white" , font=customFontRegister , borderwidth=0 ,  command=self.changeCredentialProfile)
        self.buttonChangeProfile.grid(row=7 , column=0 , columnspan=2 , pady=(20,10))

        self.Title2 = ttk.Label(self.tab5 , text="PERSONAL INFORMATION" , font="Inter 13" , foreground="white" , background="#121528")
        self.Title2.grid(row=8 , column=0 , columnspan=2 , pady=(50,0))
        
        
        iduser = usrManager.getIdUser(usernameLOGIN , passwordLOGIN)
        idusr = iduser[0]
        stringID = str(idusr) #conversione da intero a stringa per l inerimento nella label

        username = usrManager.getUsernameProfile(usernameLOGIN, passwordLOGIN)
        email = usrManager.getEmail(usernameLOGIN , passwordLOGIN)


        self.getIDuser = ttk.Label(self.tab5 , text="ID : "+stringID, font="Inter 11" , foreground="white" , background="#121528")
        self.getIDuser.grid(row= 9 , column=0 , columnspan=2 , pady=(20,10))

        self.getUsername = ttk.Label(self.tab5 , text="Username : "+username, font="Inter 11" , foreground="white" , background="#121528")
        self.getUsername.grid(row= 10 , column=0 , columnspan=2 , pady=(10,10))

        self.getEmail = ttk.Label(self.tab5 , text="Email : "+email , font="Inter 11" , foreground="white" , background="#121528")
        self.getEmail.grid(row= 11 , column=0 , columnspan=2 , pady=(10,10))

    
        self.Title = tk.Label(self.MenuFrame , text="Proxima Manger" , font=customFontSingIn , background="#1B1A36" , foreground="white")
        self.Title.pack(fill="x" , pady=40 , ipadx=14)

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

        

        self.userNameToShow=usrManager.getUsernameProfile(usernameLOGIN , passwordLOGIN)

        self.userNameProfile = tk.Label(self.AreaPersonal , text="@"+self.userNameToShow, font="Inter 12 bold" , foreground="white" , background="#111735" , padx=7 , pady=7)
        self.userNameProfile.pack(side="left")


        imgSettings = r"C:/Users/alexa/Desktop/WorkSpace/WorkSpace/Python_projects/ProximaManagerVGUI/assets/img/settings.png"
        self.imageOpen2 = Image.open(imgSettings).resize((40,40))
        self.imageSecurty = ImageTk.PhotoImage(self.imageOpen2)
        self.labelSettings = self.imageSecurty

        self.buttonSettings = tk.Button(self.AreaPersonal , image=self.labelSettings , background="#111735" , border=0 , padx=5 , pady=5 , activebackground="#111735" ,  cursor="hand2" , command=lambda:self.showTab(self.tab5))
        self.buttonSettings.pack(side="right" , padx=13 , pady=10)
        
        self.showTab(self.tab1)


    
    def logOut(self):
        from gui.main_window import MainWindow #richiamo qui per evitare problemi di loop nel routing

        self.root.destroy()
        goLogIn = tk.Tk()
        quit =  MainWindow(goLogIn)


    def showTab(self, tab_frame):
        for Widget in self.MainFrame.winfo_children():
            Widget.grid_forget()
        
        tab_frame.grid(sticky="nsew")
    

    def filterSearch(self):

        crdManager = credentialsManagement()

        valueOfStringOption = self.optionVariable.get() #opzione
        valueOfStringEntry = self.EntryFilterSearch.get() #product

        id = self.idUser[0] #TUPLA ATTENZIONE NEL CASO ESTRARRE L IDICE DELL ID NECESSARIO 

        print(f"DEBUG [ ID User: {id}, Service: {valueOfStringEntry} ]") #DEBUG PER MONITORARE IL TIPO DI VARIABILE (1,0) OUTPUT GENERA ERRORE SQL PERCHE NON E UN DATO SINGOLO MA E UNA TUPLA
        
        

        if valueOfStringOption == "SERVICE":    

            rowCrd = crdManager.filterSeacrhService(id , valueOfStringEntry)
            self.tree2.delete(*self.tree2.get_children())

            for credential in rowCrd:
                self.tree2.insert("", tk.END , values=credential)
            self.tree2.update_idletasks()

        elif valueOfStringOption == "USERNAME":

            rowCrd = crdManager.filterSearchUsername(id , valueOfStringEntry)
            self.tree2.delete(*self.tree2.get_children())

            for credential in rowCrd:
                self.tree2.insert("" , tk.END , values=credential)
            self.tree2.update_idletasks()

        elif valueOfStringOption == "EMAIL":

            rowCrd = crdManager.filterSearchEmail(id , valueOfStringEntry)
            self.tree2.delete(*self.tree2.get_children())

            for credential in rowCrd:
                self.tree2.insert("" , tk.END , values=credential)
            self.tree2.update_idletasks()

        elif valueOfStringOption == "ID CREDENTIAL":

            rowCrd = crdManager.filterSearchID(id, valueOfStringEntry)
            self.tree2.delete(*self.tree2.get_children())

            for credential in rowCrd:
                self.tree2.insert("" , tk.END , values=credential)
            self.tree2.update_idletasks()
            
    
    def startSeacrch(self):
        self.filterSearch() 


    def addCredential(self):
        
        id = self.idUser[0]

        username = self.inputVarUsername.get().strip() #.strip() controllo degli spazi vuoti
        password = self.inputVarPassword.get().strip()
        email = self.inputVarEmail.get().strip()
        product = self.inputVarProduct.get().strip()

        crd = Credential( password , username , email , product)
        crdManger = credentialsManagement()

        cred = crdManger.addCredentials(crd , id)

        credDetails = (cred,crd.username, crd.pwd, crd.email, crd.product) #pick dell utlimo ip della riga appena pushata

        print("DEBUG : Tipo di credential:", type(cred))
        print("DEBUG : Contenuto di credential:", cred)
            
        self.tree.insert("", tk.END , values=credDetails)
        self.tree.update_idletasks()

        self.inputVarUsername.set("")
        self.inputVarPassword.set("")
        self.inputVarEmail.set("")
        self.inputVarProduct.set("")
        
        messagebox.showinfo("Credential was successfully added                                                 .")


    def changeUsernameCredential(self):
        idCredential = self.inputIDVar.get()

        username = self.inputUsernameUpdate.get()
        password = self.inputPasswordUpdate.get()
        email = self.inputEmailUpdate.get()
        product = self.inputProductUpdate.get()

        filterChoose = self.manageVar.get()

        idusr = self.idUser[0]

        crdManager = credentialsManagement()
        print("DEBUG: idCredential =", idCredential)
        

        if filterChoose == "USERNAME":

            if not username == "" and idCredential > 0:

                if self.tree.exists(idCredential):
        
                    crdManager.changeUsername(idusr , idCredential , username)

                    values1 = self.tree.item(idCredential , 'values') #aggiorno con indice  e parametri indice e username
                    valUpdateUsername = (values1[0] , username , values1[2] , values1[3] , values1[4])
                    self.tree.item(idCredential , values=valUpdateUsername)

                    messagebox.showinfo("Username was correctly updated !                                                               .")

                    self.inputUsernameUpdate.set("")
                    self.inputIDVar.set(0)
                else:
                    messagebox.showerror("Database internal error!")
            
            else: 
                messagebox.showerror("Unable to change the username because the input field is empty or the ID is invalid !                                                    .")


        elif filterChoose == "PASSWORD":

            if not password == "" and idCredential > 0:
                
                if self.tree.exists(idCredential):
                    
                    crdManager.changePassword(idusr , idCredential , password)

                    values = self.tree.item(idCredential , 'values') #ricera delle colonne corrette nell tree
                    updateValues = (values[0] , values[1] , password)  #ricera delle colonne corrette nell tree con gli indici giusti
                    self.tree.item(idCredential , values=updateValues) #ricera delle colonne corrette nell tree

                    messagebox.showinfo("Password was correctly updated !                                                               .")

                    self.inputPasswordUpdate.set("")
                    self.inputIDVar.set(0)
                else:
                    messagebox.showerror("Database internal error!")
            else:
                messagebox.showerror("You have to choose an option and write the ID credential before update                                                                       .")


        elif filterChoose == "EMAIL":

            if not email == "" and idCredential > 0:

                if self.tree.exists(idCredential):

                    crdManager.changeEmail(idusr , idCredential , email)

                    values2 = self.tree.item(idCredential , 'values')
                    updateValuesEmail = (values2[0] , values2[1], values2[2] , email)
                    self.tree.item(idCredential , values=updateValuesEmail)

                    messagebox.showinfo("Username was correctly updated !                                                               .")

                    self.inputEmailUpdate.set("")
                    self.inputIDVar.set(0)
            else:
                messagebox.showerror("You have to choose an option and write the ID credential before update                                                                       .")


        elif filterChoose == "SERVICE":

            if not product == "" and idCredential > 0:
              
              if self.tree.exists(idCredential):
                  
                  crdManager.changeProduct(idusr , idCredential , product)

                  values3 = self.tree.item(idCredential , 'values')
                  updateValuesProduct = (values3[0] , values3[1] , values3[2] , values3[3] , product)
                  self.tree.item(idCredential , values=updateValuesProduct)

                  messagebox.showinfo("Password was correctly updated !                                                               .")

                  self.inputIDVar.set(0)
                  self.inputProductUpdate.set("")
            else:
                messagebox.showerror("You have to choose an option and write the ID credential before update                                                                       .")

        elif filterChoose == "CHANGE ALL":

            if not (username == "" or password == "" or email == "" or product == "") and  idCredential > 0:

                if self.tree.exists(idCredential): 

                    crdManager.changeEmail(idusr , idCredential , email)
                    crdManager.changePassword(idusr , idCredential , password)
                    crdManager.changeProduct(idusr , idCredential , product)
                    crdManager.changeUsername(idusr , idCredential , username)

                    valuesUpdateAll = (idCredential , username , password , email , product)
                    self.tree.item(idCredential , values=valuesUpdateAll)

                    messagebox.showinfo("All data was correctly updated !                                                               .")

                    self.inputIDVar.set(0)
                    self.inputEmailUpdate.set("")
                    self.inputPasswordUpdate.set("")
                    self.inputProductUpdate.set("")
                    self.inputUsernameUpdate.set("")
            else:
                 messagebox.showerror("You have to choose an option and write the ID credential before update , all the input field must be not empty                                                                       .")
        
        elif filterChoose == "":
             messagebox.showerror("You have to choose an option first from the filter menu                                                                                                               .")


    def deleteCredential(self):
        idCredential = self.inputIDVar.get()
        iduser = self.idUser[0]
        crdManager = credentialsManagement()
        
        if idCredential>0:

            if self.tree.exists(idCredential):
                crdManager.deleteCredentialByID(iduser, idCredential)

                self.tree.delete(idCredential)
                messagebox.showinfo("The credential row was correctly deleted                                                                                                            .")
                self.inputIDVar.set(0)
            else:
                messagebox.showerror("ID credential dosen't exist                                                                                                                        .")
        else:       
            messagebox.showerror("You have to insert the ID credential before to click on delete                                                                                                                        .")    


    def changeCredentialProfile(self):
        filterUpdate = self.manageVarSettings.get()

        username = self.usernameSetting.get()
        password = self.passwordSetting.get()
        email = self.emailSetting.get()

        idusr = self.idUser[0]

        usrManager = userManagement()


        if filterUpdate == "USERNAME":

            if not username == "":
                usrManager.changeUsenrame(idusr , username)
                messagebox.showinfo("Username changed                                                                                                                                            .")
                from gui.main_window import MainWindow #richiamo qui per evitare problemi di loop nel routing

                self.root.destroy()
                goLogIn = tk.Tk()
                quit =  MainWindow(goLogIn)
            else:
                messagebox.showerror("Username field can't be empty                                                                                                                              .")

        elif filterUpdate == "PASSWORD":

            if not (password == "" or len(password) < 8):
                usrManager.changePassword(idusr , password)
                messagebox.showinfo("Password changed                                                                                                                                             .")

                from gui.main_window import MainWindow 
                self.root.destroy()
                goLogIn = tk.Tk()
                quit =  MainWindow(goLogIn)
            else: 
                messagebox.showerror("Password field can't be empty or lower than 8 char                                                                                                                             .")

        elif filterUpdate == "EMAIL":
            
            if not email == "":
                usrManager.changeEmail(idusr , email)
                messagebox.showinfo("Email changed                                                                                                                                                .")

                from gui.main_window import MainWindow 
                self.root.destroy()
                goLogIn = tk.Tk()
                quit =  MainWindow(goLogIn)
            else:
                messagebox.showerror("Email field can't be empty                                                                                                                               .")
        
        elif filterUpdate == "":
                messagebox.showerror("You have to select an option from the filter menu                                                                                                       .")


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