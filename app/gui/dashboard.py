
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

        for tab in [self.tab1 ,self.tab4, self.tab5]:
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

        
        self.labelTab3 = tk.Label(self.tab3, text="TEST TAB 3")
        self.labelTab4 = tk.Label(self.tab4, text="TEST TAB 4")
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
        self.Title.grid(row = 0 , column = 2, columnspan=2 , sticky="n" , pady=80)

        self.usernameTitle = tk.Label(self.tab1 , text="Username" , font="Inter 10" ,  foreground="white" , background="#121528")
        self.usernameTitle.grid(row=1 , column=2 , columnspan=2)

        #self.showTab(self.tab1)
        self.usernameRegistration = tk.Entry(self.tab1, textvariable=self.inputVarUsername , width=42 , border=1 , bg="white" , foreground="black" , font=("Inter" , 11))
        self.usernameRegistration.grid(row=2 , column=2 ,  columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.passwordTitle =  tk.Label(self.tab1 , text="Password" , font="Inter 10" , foreground="white" , background="#121528")
        self.passwordTitle.grid(row=3 , column=2 , columnspan=2)

        self.passwordRegistration = tk.Entry(self.tab1, textvariable=self.inputVarPassword , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.passwordRegistration.grid(row=4 , column=2 , columnspan=2 , pady=(0,10), ipadx=30, ipady=7)

        self.emailTitle = tk.Label(self.tab1 ,  text="Email" , font="Inter 10" , foreground="white" , background="#121528")
        self.emailTitle.grid(row=5 , column=2 ,  columnspan=2 )

        self.emailRegistration = tk.Entry(self.tab1, textvariable=self.inputVarEmail , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.emailRegistration.grid(row = 6 , column=2 ,  columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.productTitle = tk.Label(self.tab1 ,  text="Service" , font="Inter 10" , foreground="white" , background="#121528")
        self.productTitle.grid(row = 7 , column=2 ,  columnspan=2)

        self.productRegistration = tk.Entry(self.tab1, textvariable=self.inputVarProduct , width=42 , font=("Inter",11) , border=1 , bg="white" , foreground="black")
        self.productRegistration.grid(row = 8 , column=2 , columnspan=2 , pady=(0,10) , ipadx=30, ipady=7)

        self.buttonAdd = tk.Button(self.tab1 , text="Add Credential" , bg="#0787FF" , takefocus=0 , width=26 , height=2 , foreground="white" , font=customFontRegister , borderwidth=0 , command=self.addCredential)
        self.buttonAdd.grid(row=9 , column=2 , columnspan=2 , pady=(20,0))



        #VIEW ALL CREDENTIALS TAB#

        self.tree = ttk.Treeview(self.tab2 , column=("ID" , "USERNAME" , "PASSWORD" , "EMAIL" , "SERVICE") , show='headings')
        
        
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1" , text="ID")
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
                self.tree.insert("",tk.END , values=row)




       #FILTER SEARCH TAB
       #, ipadx=40, ipady=7  [x] lunghezza [y] altezza

        self.EntryFilterSearch = tk.Entry(self.tab3 , width=34 , font=("Inter" , 10) , background="white" , foreground="black")
        self.EntryFilterSearch.grid(row=1 , column=0 , sticky="n" , pady=(100,0) , ipadx=40, ipady=7)

        self.optionVariable = StringVar()
        self.optionVariable.set("Filters")

        self.optionList = ['ID CREDENTIAL' , 'USERNAME' , 'EMAIL' , 'SERVICE']


        self.openMenuChoose = tk.OptionMenu(self.tab3 , self.optionVariable , * self.optionList)
        self.openMenuChoose.config(border=0)
        self.openMenuChoose.grid(row=1 , column=0, sticky="n" ,padx=(0,450), pady=(101,0) , ipady=3)

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


    def db_connect(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "rootALEX",
            password = "root2234A03", #CHANGE
            database = "credentials_management"
        )
    

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
        
        messagebox.showinfo("Credential was successfully added                     .")


 



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