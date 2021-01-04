
if __name__ == "__main__":
    print("""
    Acciones disponibles:
        1 - Registro
        2 - Login
    """)

    accion = int(input('que quieres hacer: '))

    if accion == 1:
        print("Ok, vamos a resitararnos en el sistemas")
        nombre = input('cual es tu nombre?: ')
        apellidos = input('cuales osn tus apellidos?: ')
        email = input('cual es tu email?: ')
        password = input('ingresa tu contraseña: ')

    elif accion == 2:
        print("Ok, vamos a iniciar seccion")
        email = input('cual es tu email?: ')
        password = input('cual es tu contraseña: ')