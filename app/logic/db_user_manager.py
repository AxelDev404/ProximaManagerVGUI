
import mysql.connector 
from mysql.connector import Error



class userManagement():

    def connection(self):
        return mysql.connector.connect(
            host = "localhost" , 
            user = "rootALEX" , 
            password = "root2234A03",
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