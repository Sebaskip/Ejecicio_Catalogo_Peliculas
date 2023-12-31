from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp
from Dominio.Pelicula import Pelicula
opcion = None
while opcion != 4:
    try:
        print(f'''
Opciones:
1. Agregar pelicula
2. Listar peliculas
3. Eliminar catalogo
4. Salir
''')
        opcion = int(input(f'Escribe tu opcion (1-4): '))
        if opcion == 1:
            nombre_pelicula = input(f'Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print(f'Salimos del programa')