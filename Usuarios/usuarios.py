import datetime
import hashlib
from Usuarios import conexion as conexio

conex = conexio.connector()
database = conex[0]
cursor = conex[1]

class Usuarios:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def Registrar(self):
        
        #cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        fecha = datetime.datetime.now()
        sql = "insert into usuarios values(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self. email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
    
    def Identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "
        
        #cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usurio = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usurio)
        result = cursor.fetchone()

        return result
