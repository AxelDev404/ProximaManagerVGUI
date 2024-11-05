import mysql.connector 
from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk

class credentialsManagement():

    def db_connect(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "rootALEX",
            password = "root2234A03",
            database = "credentials_management"
        )


    def viewAllCredentials(self , idUser):

        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "SELECT id_credential , username , pwd , email , product FROM credentials WHERE id_user_credentials = %s"
        cursor.execute(sqlQuery , idUser,)

        user = cursor.fetchall()

        cursor.close()
        db.close()

        if user:
            return user
        else:
            print("Fatal error to give the credentials")


    def filterSeacrhService(self, idUser , service):

        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "SELECT id_credential , username , pwd, email , product FROM credentials WHERE id_user_credentials = %s AND product = %s"
        cursor.execute(sqlQuery, (idUser,service))

        crd = cursor.fetchall()
        cursor.close()
        db.close()

        if crd:
            return crd
        else:
            print("DEBUG : Fatal error to give credentials")
        

    def filterSearchUsername(self, idUser , username):
        
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "SELECT id_credential , username , pwd , email , product FROM credentials WHERE id_user_credentials = %s AND username = %s"

        cursor.execute(sqlQuery , (idUser , username))
        crd = cursor.fetchall()

        cursor.close()
        db.close()

        if crd:
            return crd
        else:
            print("DEBUG : Fatal error to give credentials")


    def filterSearchEmail(self, idUser , email):

        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "SELECT id_credential , username , pwd , email , product FROM credentials WHERE id_user_credentials = %s AND email = %s"
        cursor.execute(sqlQuery , (idUser , email))

        crd = cursor.fetchall()
        cursor.close()
        db.close()

        if crd:
            return crd
        else:
            print("Fatal error to give credentials")


    def filterSearchID (self, idUser , idCredentials):
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "SELECT id_credential , username , pwd , email , product FROM credentials WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (idUser , idCredentials))
        crd = cursor.fetchall()

        cursor.close()
        db.close()

        if crd:
            return crd
        else:
            print("Fatal error to give credentials")


    def addCredentials(self , crd , idUser):
        
        values = (idUser , crd.username , crd.pwd , crd.email , crd.product)
        print(f"Debug: Stai per inserire i valori: {values}")
        
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "INSERT INTO credentials (id_user_credentials , username , pwd , email , product) VALUES (%s , %s , %s , %s , %s)"
        cursor.execute(sqlQuery , values)

        idCredential = cursor.lastrowid


        db.commit()
        print("Dati inseriti nel database:", values)
        cursor.close()
        db.close()

        return idCredential
    

    def changeUsername(self , idUser , idCredential , updateUsername):
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "UPDATE credentials SET username = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (updateUsername , idUser , idCredential))
        db.commit()
        
        cursor.close()
        db.close()

        

        if cursor.rowcount>0:
            print("DEBUG : username was updated!")
        else:
            print("DEBUG : username can't be updated!")


    def changePassword(self , idUser , idCredential , updatePassword):
        db = self.db_connect()
        cursor = db.cursor()
        
        sqlQuery = "UPDATE credentials SET pwd = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (updatePassword , idUser , idCredential))
        db.commit()

        cursor.close()
        db.close()

        if cursor.rowcount>0:
            print("DEBUG : Password was updated!")
        else:
            print("DEBUG : Password can't be updated!")

    
    def changeEmail(self , idUser , idCredential , updateEmail):
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "UPDATE credentials SET email = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (updateEmail , idUser , idCredential))
        db.commit()

        cursor.close()
        db.close()

        if cursor.rowcount>0:
            print("DEBUG : Email was correctly updated")
        else:
            print("DEBUG : Email can't be updated")


    def changeProduct(self , idUser , idCredential , updateProduct):
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "UPDATE credentials SET product = %s WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (updateProduct , idUser , idCredential))
        db.commit()

        cursor.close()
        db.close()

        if cursor.rowcount > 0:
            print("DEBUG : product was correctly updated!")
        else:
            print("DEBUG : product can't be updated!")

    def deleteCredentialByID(self, idUser , idCredential):
        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "DELETE FROM credentials WHERE id_user_credentials = %s AND id_credential = %s"
        cursor.execute(sqlQuery , (idUser , idCredential))
        db.commit()
        cursor.close()
        db.close()

        if cursor.rowcount>0:
            print("DEBUG : Credential was corectly deleted!")
        else:
            print("DEBUG : Credential can't be deleted!")