# ProximaManagerVGUI
GUI version of ProximaManager 


INSTRUCTION :

1] Create the database from mysql shell

2] Execute the sql scritp in DataBase folder (You have to connect mysql to your machine first) 

3] Put your mysql password and username in db_credential_management , db_user_managemet classes  



4] Launch in the VsCode terminal this command to create the executable file (navigate with the terminal in the principal folder than you can execute the command on terminal, Just copy all and paste)
 
  pyinstaller --onefile --noconsole --icon=assets/icons/iconPass.ico `
  --add-data "app/gui;gui" `
  --add-data "app/logic;logic" `
  --add-data "assets/fonts/TechNoir-8dLD.ttf;assets/fonts" `
  --add-data "assets/icons/iconPass.ico;assets/icons" `
  --add-data "assets/img/account-protection.png;assets/img" `
  --add-data "assets/img/cyber.png;assets/img" `
  --add-data "assets/img/login-.png;assets/img" `
  --add-data "assets/img/logout.png;assets/img" `
  --add-data "assets/img/magnifying-glass.png;assets/img" `
  --add-data "assets/img/settings.png;assets/img" `
  --hidden-import=tkinter.ttk `
  --hidden-import=tkinter.messagebox `
  --hidden-import=ctypes `
  --hidden-import=PIL `
  --hidden-import=PIL.Image `
  --hidden-import=PIL.ImageTk `
  --hidden-import=mysql.connector `
  app\ProximaManager.py








LogIn Pannel : 

![logInProximaManager](https://github.com/user-attachments/assets/6253b1af-1bad-4090-9e61-5444db73cfe7)


--------------------------------------------------------------------------------------------------------------------------------------------

Sing Up Pannel : 

![SingUpProximaManager](https://github.com/user-attachments/assets/df0aee23-a500-45d5-a6e4-b229483e31fa)


--------------------------------------------------------------------------------------------------------------------------------------------

Dashboard : 

![DashBoardProximaManager](https://github.com/user-attachments/assets/c08f6d65-82ef-4b24-943d-7281988d4cda)


--------------------------------------------------------------------------------------------------------------------------------------------

Add credentials : 

![DashBoardProximaManager](https://github.com/user-attachments/assets/15a94797-ce37-417f-a7b7-24a3c67cd3b8)

--------------------------------------------------------------------------------------------------------------------------------------------

Filter search :

![ProximaFilter](https://github.com/user-attachments/assets/7b8681c3-c744-4e60-ba1f-6ee4badc0666)


--------------------------------------------------------------------------------------------------------------------------------------------

View all credentials :

![proximaNewScreenViewAll](https://github.com/user-attachments/assets/6e1c069d-60d3-4f3e-ad41-b7e0e77eb747)


Manage Credentials :

![ProximaAddANDDelet](https://github.com/user-attachments/assets/87f2a905-b514-42eb-841a-31f778404ecf)

Profile Settings : 

![ProximaSettings](https://github.com/user-attachments/assets/5dc1fe73-8981-429c-92e3-e233387c1bf3)



Developed by AxelDev404 

The rights are reserved for AxelDev404, if someone sold you this program it means that you have been scammed.


