import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'admin'
        self.database = 'vingadores'
   
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
            )
            self.cursor = self.connection.cursor()
            print('Conexão com o banco de dados realizada com sucesso ')
        except Error as e:
            print(f'Error: {e}')
            return None

Database().connect()
#db = Database()
#db.connect()