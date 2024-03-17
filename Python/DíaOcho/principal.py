import turnos

menu_opciones = "\n[1] Cosmetología\n" \
                "[2] Farmacia\n" \
                "[3] Perfumería\n"

while True:
    print(menu_opciones)
    seleccion = int(input("Seleccione un área para obtener su turno: "))

    if seleccion == 1:
        turnos.decorador(seleccion)

    if seleccion == 2:
        turnos.decorador(seleccion)

    if seleccion == 3:
        turnos.decorador(seleccion)

    if seleccion != 1 and seleccion != 2 and seleccion != 3:
        seleccion = input("Seleccione una opción correcta: ")
