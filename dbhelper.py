<<<<<<< HEAD
import mysql.connector
class Databasehelper:
    def __init__(self)->None:
        self.host = 'localhost'
        self.user = 'root@localhost'
        self.password = ''
        self.database = 'users'

    def getdb_connection(self):
        connection = mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )
        return connection

    def getall_users(self, query:str):
        connection = self.getdb_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return users
=======
from mysql.connector import connect

def dbconnect()->None:
    return connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='users'
    )
    
def getall_users()->list:
    sql:str = f"SELECT * FROM `users`"
    db:object = dbconnect()
    cursor:object = db.cursor(dictionary=True)
    cursor.execute(sql)
    data:list = cursor.fetchall()
    return data
    
def validate_user(username:str,password:str)->list:
    sql:str = f"SELECT * FROM `users` WHERE `username`= {username} AND `password`= {password}"
    db:object = dbconnect()
    cursor:object = db.cursor(dictionary=True)
    cursor.execute(sql)
    data:list = cursor.fetchall()
    return data

    
>>>>>>> d415e64e731f1483a43a14f2280e77146f9cf82e
