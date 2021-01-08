from Usuarios import conexion as conexio

conex = conexio.connector()
database = conex[0]
cursor = conex[1]

class Nota:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self. descripcion = descripcion

    
    def guardar(self):
        sql ='INSERT INTO notas VALUES(null, %s, %s, %s, NOW())'
        nota = (self.usuario_id, self.titulo, self.descripcion)

        try:
            cursor.execute(sql, nota)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

