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

        