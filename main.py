from usuarios import acciones

if __name__ == "__main__":
    print("""
    Acciones disponibles:
        1 - Registro
        2 - Login
    """)

    accion = int(input('que quieres hacer: '))
    haz_el = acciones.Acciones()

    if accion == 1:
        haz_el.Registro()
    elif accion == 2:
        haz_el.Login()