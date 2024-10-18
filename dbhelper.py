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