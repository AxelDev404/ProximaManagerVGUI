
import mysql.connector 
from mysql.connector import Error
from tkinter import messagebox


class userManagement():

    def connection(self):
        return mysql.connector.connect(
            host = "localhost" , 
            user = "username" , 
            password = "password",
            database = "credentials_management"
            #auth_plugin='mysql_native_password'
        )


    def logIn(self , username , password):

        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "SELECT id_user FROM user WHERE username = %s AND pwd = %s"

        cursor.execute(sqlQuery , (username , password))

        usr = cursor.fetchone()
        db.close()
        cursor.close()

        if usr:
            return True
        else:
            print("Failed LOGIN invalid credetials")
        
        
    def getUsernameProfile(self, username , pasword):
        db = self.connection()
        curosr = db.cursor()

        sqlQuery = "SELECT username FROM user WHERE username = %s AND pwd = %s"
        curosr.execute(sqlQuery, (username , pasword))

        usr = curosr.fetchone()
        curosr.close()
        db.close()

        if usr : 
            userN = usr[0]
            return userN
        
    def getIdUser(self , username , password):

        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "SELECT id_user FROM user WHERE username = %s AND pwd = %s"
        cursor.execute(sqlQuery , (username , password))
    
        usr = cursor.fetchall()
        cursor.close()
        db.close()

        if usr:
            userId = usr[0]
            return userId
        else:
            print("Failed LogIn")

    def signIn (self, user):
        values = (user.nome , user.username , user.pwd , user.email , user.number_phone )

        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "INSERT INTO user (nome , username , pwd , email , number_phone) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sqlQuery , values)

        db.commit()

        cursor.close()
        db.close()

    
    def checkExistanceUserinDb(self , username , email):
        controllExistance = False

        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "SELECT username , email FROM user WHERE username = %s OR email = %s"
        cursor.execute(sqlQuery , (username,email))

        usr = cursor.fetchone()
        cursor.close()
        db.close()

        messagebox.showinfo("Registration is complete")

        if usr:
            controllExistance = True
            messagebox.showerror("Can't create the accout because the email is alredy in use")
            return controllExistance
        else:
            controllExistance = False
            return controllExistance
        
        
    def getEmail(self , username , password): 
        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "SELECT email FROM user WHERE username = %s AND pwd = %s"
        cursor.execute(sqlQuery , (username , password))

        usr = cursor.fetchone()
        cursor.close()
        db.close()

        if usr:
            email = usr[0]
            return email 
        else:
            print("DEBUG : Cant get the email from user")

    
    def changeUsenrame(self , idusr , usernameToUpdate):
        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "UPDATE user SET username = %s WHERE id_user = %s"
        cursor.execute(sqlQuery , (usernameToUpdate , idusr))
        db.commit()

        usr =  cursor.fetchone()

        cursor.close()
        db.close()

        if usr:
            print("DEBUG : Username was correctly changed")
        else:
            print("DEBUG : Unable to change the username")

    
    def changePassword(self, idusr , passwordToUpdate):
        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "UPDATE user SET pwd = %s WHERE id_user = %s"
        cursor.execute(sqlQuery , (passwordToUpdate , idusr))
        db.commit()

        usr = cursor.fetchone()

        cursor.close()
        db.close()

        if usr: 
            print("DEBUG : Password was correctly changed")
        else:
            print("DEBUG : Unable to change the Password")


    def changeEmail(self, idusr , emailToUpdate):
        db = self.connection()
        cursor = db.cursor()

        sqlQuery = "UPDATE user SET email = %s WHERE id_user = %s"
        cursor.execute(sqlQuery , (emailToUpdate , idusr))
        db.commit()

        usr = cursor.fetchone()

        cursor.close()
        db.close()

        if usr:
            print("DEBUG : email was correctly changed")
        else:
            print("DEBUG : Unable to change the email")