precios_cafe = [('Frappe', 85), ('Mocha Blanco', 90), ('Espresso', 55)]

for elemento in precios_cafe:
    print(elemento)

for cafe, precio in precios_cafe:
    print(cafe)

for cafe, precio in precios_cafe:
    print(precio * .50)


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_costoso = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_costoso = cafe
        else:
            pass

    return cafe_mas_costoso, precio_mayor


cafe, precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es el {cafe}. Y cuesta ${precio}.")
