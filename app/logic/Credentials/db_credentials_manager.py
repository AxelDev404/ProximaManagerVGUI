import mysql.connector 
from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk

class credentialsManagement():

    def db_connect(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "rootAlex",
            password = "root2003A03",
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

        db = self.db_connect()
        cursor = db.cursor()

        sqlQuery = "INSERT INTO credentials (id_user_credentials , username , pwd , email , product) VALUES (%s , %s , %s , %s , %s)"
        cursor.execute(sqlQuery , (values))

        db.commit()

        cursor.close()
        db.close()