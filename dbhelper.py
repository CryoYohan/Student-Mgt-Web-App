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

    