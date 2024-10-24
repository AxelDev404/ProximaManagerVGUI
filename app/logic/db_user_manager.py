
import mysql.connector 
from mysql.connector import Error
import pymysql


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
        
        
    
        
        