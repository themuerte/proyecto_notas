import usuarios.usuarios as modelo
class Acciones:
    
    def Registro(self):
        print("Ok, vamos a resitararnos en el sistemas")
    
        nombre = input('cual es tu nombre?: ')
        apellidos = input('cuales osn tus apellidos?: ')
        email = input('cual es tu email?: ')
        password = input('ingresa tu contraseña: ')

        usuario = modelo.Usuarios(nombre, apellidos, email, password)
        registro = usuario.Registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has rgsitrado correctamente")
        else:
            print(f"{registro[1].nombre}NO te has rgsitrado correctamente")

    def Login(self):
        print("Ok, vamos a iniciar seccion")
        
        email = input('cual es tu email?: ')
        password = input('cual es tu contraseña: ')

