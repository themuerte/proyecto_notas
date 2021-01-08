import Notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nueva nota")
        print('')
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce la descripcion: ")
        print('')

        notas_obj = modelo.Nota(usuario[0], titulo, descripcion)
        nota_creada = notas_obj.guardar()
        
        if nota_creada[0] >= 1:
            print(f"Perfecto {usuario[1]} se ha creado su nota correctamente")
        else:
            print(f"{usuario[1]} NO se ha creado su nota")

    def Mostrar(self, usuario):
    
        notas_obj = modelo.Nota(usuario[0], ' ', ' ')
        mostrar = notas_obj.listar()

        
        print(f"{usuario[1]}!! estas son tus notas")
        print('')
        for nota in mostrar:
            print(nota[2])
            print(nota[3])
            print("********************************")

    def Eliminar(self, usuario):
        nota_eliminar = input('Ingrese el titulo de la nota que quiere eliminar: ')
        print('')

        notas_obj = modelo.Nota(usuario[0], nota_eliminar, '')
        nota_eliminada = notas_obj.eliminar()

        if nota_eliminada[0] >= 1:
            print(f"Perfecto {usuario[1]} se ha eliminado su nota correctamente")
        else:
            print(f"{usuario[1]} NO se ha eliminado su nota")
        