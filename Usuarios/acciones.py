import Usuarios.usuarios as modelo

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
        
        try:
            email = input('cual es tu email?: ')
            password = input('cual es tu contraseña: ')

            usurio = modelo.Usuarios('', '', email, password)
            login = usurio.Identificar()
            print(login)

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has regitrado {login[5]}")
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"login incorrecto")
