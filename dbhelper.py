import mysql.connector as mariadb
class Databasehelper:
    def __init__(self)->None:
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'users'
        self.table = "students"

    def getdb_connection(self):
        connection = mariadb.connect(
            host= self.host,
            user= self.user,
            password= self.password,
            database= self.database
        )
        return connection
    
    def getprocess(self,sql:str):
        connection = self.getdb_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        data:list = cursor.fetchall()
        cursor.close()
        connection.close()
        return data

    def postprocess(self,sql:str):
        connection = self.getdb_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close() 

    def getall_students(self)->list:
        query = f"SELECT * FROM {self.table}"
        users:list = self.getprocess(query)
        return users
    
    def find_users(self,idno:str):
        connection = self.getdb_connection()
        cursor:object = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM users WHERE `idno` = {idno}")
        data:list = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
    
    def add_students(self,**kwargs):
        keys:list = kwargs.keys()
        values:list=kwargs.values()
        columns:str = ",".join(keys)
        formatted_values = ",".join([f"'{v}'" if isinstance(v, str) else str(v) for v in values])
        sql:str = f"INSERT INTO {self.table} ({columns}) VALUES({formatted_values})"
        return self.postprocess(sql)
