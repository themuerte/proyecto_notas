import mysql.connector
import datetime

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Qwsxzaqwedc1!',
    database = 'master_python',
    port = 3306

)

cursor = database.cursor(buffered=True)

class Usuarios:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def Registrar(self):
        fecha = datetime.datetime.now()
        sql = "insert into usuarios values(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self. email, self.password, fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
    
    def Identificar(self):
        self.nombre

