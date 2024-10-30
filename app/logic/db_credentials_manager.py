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

        return crd
   
        print("Fatal error to give credentials")