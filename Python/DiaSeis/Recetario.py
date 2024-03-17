import os
import pathlib
from os import system
from colorama import Fore

ruta_principal = "/Users/claudiainzunza/Desktop/Recetas"
numero_recetas = 0

for root_dir, cur_dir, archivos in os.walk(ruta_principal):
    numero_recetas += len(archivos)

print(Fore.LIGHTWHITE_EX + f"¡Bienvenido a su recetario! La ruta de acceso "
                           f"a su recetario es la siguiente: " + Fore.RED + f"{ruta_principal}.")
print(Fore.LIGHTWHITE_EX + f"Actualmente cuenta con un total de {numero_recetas} recetas.\n")


def menu_principal():
    lista_opciones = [1, 2, 3, 4, 5, 6]

    menu = "[1] Leer receta\n[2] Crear receta\n[3] Crear categoría\n" \
           "[4] Eliminar receta\n[5] Eliminar categoría\n[6] Finalizar programa\n"

    print(Fore.LIGHTBLUE_EX + menu)
    seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una opción del menú: "))
    system('clear')

    while seleccion not in lista_opciones:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.LIGHTBLUE_EX + menu)
        seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una opción del menú: "))
        system('clear')

    return seleccion


def elegir_categoria(ruta):
    directorio = pathlib.Path(ruta)
    numero_de_opciones = []
    lista_opciones = []
    menu = ""
    i = 1

    for archivo in directorio.iterdir():
        if archivo.is_file:
            pass

        if archivo.is_dir:
            lista_opciones.append(archivo.stem)
            numero_de_opciones.append(i)
            i += 1

    lista_opciones.sort()
    lista_opciones.pop(0)
    numero_de_opciones.pop(-1)

    for num, opc in zip(numero_de_opciones, lista_opciones):
        menu = menu + f"[{num}] {opc}\n"

    print(Fore.CYAN + menu)
    seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una categoría: "))
    cat = lista_opciones[seleccion - 1]
    system('clear')

    while seleccion not in numero_de_opciones:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.CYAN + menu)
        seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una categoría: "))
        system('clear')

    return cat


def leer_receta(cat):
    ruta = '/Users/claudiainzunza/Desktop/Recetas/' + f'{cat}'

    directorio = pathlib.Path(ruta)
    lista_recetas = []
    numero_de_opciones = []
    menu = ""
    i = 1

    for archivo in directorio.iterdir():
        if archivo.is_file:
            lista_recetas.append(archivo.stem)
            numero_de_opciones.append(i)
            i += 1

        if archivo.is_dir:
            pass

    lista_recetas.sort()

    for num, opc in zip(numero_de_opciones, lista_recetas):
        menu = menu + f"[{num}] {opc}\n"

    print(Fore.YELLOW + menu)
    seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una receta para leer: "))
    system('clear')

    while seleccion not in numero_de_opciones:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.YELLOW + menu)
        seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija una receta para leer: "))
        system('clear')

    num_receta = seleccion - 1
    ruta_receta = ruta + f"/{lista_recetas[num_receta]}"
    inf_receta = open(ruta_receta + ".txt")
    print(inf_receta.read())
    inf_receta.close()


def crear_receta(ruta):
    directorio = pathlib.Path(ruta)
    lista_categorias = []
    numero_de_opciones = []
    menu = ""
    i = 1

    for archivo in directorio.iterdir():
        if archivo.is_file:
            pass

        if archivo.is_dir:
            lista_categorias.append(archivo.stem)
            numero_de_opciones.append(i)
            i += 1

    lista_categorias.sort()
    lista_categorias.pop(0)

    for num, opc in zip(numero_de_opciones, lista_categorias):
        menu = menu + f"[{num}] {opc}\n"

    print(Fore.YELLOW + menu)
    categoria = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría de su receta: "))
    system('clear')

    while categoria not in numero_de_opciones:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.YELLOW + menu)
        categoria = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría de su receta: "))
        system('clear')

    num_categoria = categoria - 1
    ruta_categoria = ruta + f"/{lista_categorias[num_categoria]}"
    print(Fore.RED + f"Ha seleccionado la categoría '{lista_categorias[num_categoria]}'.\n")

    nombre_receta = input(Fore.LIGHTWHITE_EX + "Escriba el nombre de la receta a crear: ")
    archivo_receta = open(ruta_categoria + f'/{nombre_receta}.txt', 'a')
    receta = input("Escriba su receta: ")
    print(Fore.RED + "¡Receta crada con éxito!")
    archivo_receta.write(receta)
    archivo_receta.close()


def crear_categoria(ruta):
    nombre_categoria = input("Escriba el nombre de la categoría a crear: ")
    os.makedirs(ruta + '/' + nombre_categoria)
    print(Fore.RED + f"¡Categoría '{nombre_categoria}' creada con éxito!")


def eliminar_receta(ruta):
    directorio_categorias = pathlib.Path(ruta)
    lista_categorias = []
    numero_de_categorias = []
    menu = ""
    i = 1

    for archivo in directorio_categorias.iterdir():
        if archivo.is_file:
            pass

        if archivo.is_dir:
            lista_categorias.append(archivo.stem)
            numero_de_categorias.append(i)
            i += 1

    lista_categorias.sort()
    lista_categorias.pop(0)

    for num, opc in zip(numero_de_categorias, lista_categorias):
        menu = menu + f"[{num}] {opc}\n"

    print(Fore.YELLOW + menu)
    cat = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría de la receta que desea eliminar: "))
    system('clear')

    while cat not in numero_de_categorias:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.YELLOW + menu)
        cat = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría de la receta que desea eliminar: "))
        system('clear')

    num_categoria = cat - 1
    ruta_categoria = ruta + f"/{lista_categorias[num_categoria]}"

    directorio_recetas = pathlib.Path(ruta_categoria)
    lista_recetas = []
    numero_de_recetas = []
    menu_recetas = ""
    i = 1

    for archivo in directorio_recetas.iterdir():
        if archivo.is_file:
            lista_recetas.append(archivo.stem)
            numero_de_recetas.append(i)
            i += 1

        if archivo.is_dir:
            pass

    lista_recetas.sort()

    for num, opc in zip(numero_de_recetas, lista_recetas):
        menu_recetas = menu_recetas + f"[{num}] {opc}\n"

    print(Fore.YELLOW + menu_recetas)
    seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija la receta que desea eliminar: "))
    system('clear')

    while seleccion not in numero_de_recetas:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.YELLOW + menu_recetas)
        seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija la receta que desea eliminar: "))
        system('clear')

    num_receta = seleccion - 1
    os.remove(ruta_categoria + f"/{lista_recetas[num_receta]}.txt")
    print(Fore.RED + "¡Se ha eliminado la receta con éxito!")


def eliminar_categoria(ruta):
    directorio = pathlib.Path(ruta)
    numero_de_opciones = []
    lista_opciones = []
    menu = ""
    i = 1

    for archivo in directorio.iterdir():
        if archivo.is_file:
            pass

        if archivo.is_dir:
            lista_opciones.append(archivo.stem)
            numero_de_opciones.append(i)
            i += 1

    lista_opciones.sort()
    lista_opciones.pop(0)
    numero_de_opciones.pop(-1)

    for num, opc in zip(numero_de_opciones, lista_opciones):
        menu = menu + f"[{num}] {opc}\n"

    print(Fore.CYAN + menu)
    seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría que desea eliminar: "))
    system('clear')

    while seleccion not in numero_de_opciones:
        print(Fore.RED + "¡Opción inválida!\n")
        print(Fore.CYAN + menu)
        seleccion = int(input(Fore.LIGHTWHITE_EX + "Elija la categoría que desea eliminar: "))
        system('clear')

    categoria = lista_opciones[seleccion - 1]
    '''ruta_categoria = ruta + f"/{categoria}"'''
    os.rmdir(ruta + f"/{categoria}")
    print(Fore.RED + f"¡Categoría '{categoria}' eliminada con éxito!")


def terminar_programa():
    print(Fore.RED + "El programa ha finalizado.")
    exit()


seleccion_principal = menu_principal()

if seleccion_principal == 1:
    categoria = elegir_categoria(ruta_principal)
    leer_receta(categoria)
if seleccion_principal == 2:
    crear_receta(ruta_principal)
if seleccion_principal == 3:
    crear_categoria(ruta_principal)
if seleccion_principal == 4:
    eliminar_receta(ruta_principal)
if seleccion_principal == 5:
    eliminar_categoria(ruta_principal)
if seleccion_principal == 6:
    terminar_programa()
