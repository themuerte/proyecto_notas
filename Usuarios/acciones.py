import Usuarios.usuarios as modelo
from Notas import acciones

class Acciones:
    
    def Registro(self):
        print("Ok, vamos a resitararnos en el sistemas")
        print()
        nombre = input('cual es tu nombre?: ')
        apellidos = input('cual es tu apellido?: ')
        email = input('cual es tu email?: ')
        password = input('ingresa tu contraseña: ')
        print()
        
        usuario = modelo.Usuarios(nombre, apellidos, email, password)
        registro = usuario.Registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado correctamente")
        else:
            print(f"{registro[1].nombre} NO te has registrado")

    def Login(self):
        print("Ok, vamos a iniciar seccion")
        print()

        try:
            email = input('cual es tu email?: ')
            password = input('cual es tu contraseña: ')
            print()

            usurio = modelo.Usuarios('', '', email, password)
            login = usurio.Identificar()
            

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has regitrado {login[5]}")
                self.aproximizaciones(login)
        
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"login incorrecto")
    
    def aproximizaciones(self, usuario):
 
        print("""
        Acciones disponibles:
        1 - Crear notas
        2 - Mostrar notas
        3 - Eliminar notas 
        99 - Salir
        """)

        accion = int(input('que quieres hacer?: '))
        haz = acciones.Acciones()

        if accion == 1:
            print('Crear notas')
            haz.crear(usuario)
            self.aproximizaciones(usuario)

        elif accion == 2:
            print('Mostrar notas')
            self.aproximizaciones(usuario)

        elif accion == 3:
            print('Eliminar notas')
            self.aproximizaciones(usuario)
            
        elif accion == 99:
            exit()

        return None 

