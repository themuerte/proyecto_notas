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

    def listar(self):
        sql = f"SELECT * FROM notas WHERE id_usuarios = {self.usuario_id}"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except:
            print("F")
        
        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuarios_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        
        try:
            cursor.execute(sql)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

