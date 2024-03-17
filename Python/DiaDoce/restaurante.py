from tkinter import *

operador = ''
precios_comida = [125, 150, 200, 350, 220, 310, 230, 500]
precios_bebida = [67, 89, 35, 100, 60, 40, 500, 350]
precios_postres = [200, 400, 350, 450, 230, 90, 75, 68]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x1 = 0
    for c in cuadros_comida:
        if variables_comida[x1].get() == 1:
            cuadros_comida[x1].config(state=NORMAL)
            cuadros_comida[x1].focus()
            if cuadros_comida[x1].get() == '0':
                cuadros_comida[x1].delete(0, END)
        else:
            cuadros_comida[x1].config(state=DISABLED)
            texto_comida[x1].set('0')
        x1 += 1

    x2 = 0
    for c in cuadros_bebida:
        if variables_bebida[x2].get() == 1:
            cuadros_bebida[x2].config(state=NORMAL)
            cuadros_bebida[x2].focus()
            if cuadros_bebida[x2].get() == '0':
                cuadros_bebida[x2].delete(0, END)
        else:
            cuadros_bebida[x2].config(state=DISABLED)
            texto_bebida[x2].set('0')
        x2 += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            cuadros_postre[x].focus()
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1


def total():
    subtotal_comida = 0
    x = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (int(cantidad.get()) * precios_comida[x])
        x += 1
    print(subtotal_comida)

# Inicar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1175x510+0+0')

# Título de ventana
aplicacion.title("Sistema de facturación")

# Evitar maximizar
aplicacion.resizable(0, 0)

# Color de fondo
aplicacion.config(bg='White')

# Panel superior
panel_superior = Frame(aplicacion, bd=0, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta que irá dentro del panel
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de facturación',
                        fg='black',
                        font=('Dosis', 58),
                        bg='White',
                        width=27)

etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=0, relief=FLAT, padx=5, pady=13)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=5, bg='DarkGrey', relief=FLAT, padx=48, pady=5)
panel_costos.pack(side=BOTTOM, pady=10)

# Panel comidas (LabelFrame trae incorporada la etiqueta)
panel_comidas = LabelFrame(panel_izquierdo,
                           text='Comida',
                           font=('Dosis', 19, 'bold'),
                           bd=0,
                           relief=FLAT,
                           fg='black')
panel_comidas.pack(side=LEFT)

# Panel bebidas (LabelFrame trae incorporada la etiqueta)
panel_bebidas = LabelFrame(panel_izquierdo,
                           text='Bebidas',
                           font=('Dosis', 19, 'bold'),
                           bd=0,
                           relief=FLAT,
                           fg='black')
panel_bebidas.pack(side=LEFT)

# Panel postres (LabelFrame trae incorporada la etiqueta)
panel_postres = LabelFrame(panel_izquierdo,
                           text='Postres',
                           font=('Dosis', 19, 'bold'),
                           bd=0,
                           relief=FLAT,
                           fg='black')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion,
                      bd=0,
                      relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel recibo
panel_recibo = Frame(panel_derecha,
                     bd=0,
                     relief=FLAT,
                     bg='LightSteelBlue')
panel_recibo.pack()

# Panel calculadora
panel_calculadora = Frame(panel_derecha,
                          bd=0,
                          relief=FLAT,
                          bg='LightSteelBlue')
panel_calculadora.pack()

# Panel botones
panel_botones = Frame(panel_derecha,
                      bd=0,
                      relief=FLAT,
                      bg='LightSteelBlue')
panel_botones.pack()

# Lista de prpductos
lista_comidas = ['Sushi', 'Pollo asado', 'salmón', 'Ensalada de papas', 'Pizza de pepperoni', 'Espagueti',
                 'Carne asada', 'Tacos al pastor']
lista_bebidas = ['Agua natural', 'Coca-Cola', 'Chocolate caliente', 'Malteada de fresa', 'Vino blanco', 'Vino tinto',
                 'Cerveza', 'Tequila']
lista_postres = ['Pastel de chocolate', 'Flan', 'Gelatina', 'Brownies', 'Mousse de chocolate', 'Helado', 'Galletas',
                 'Mangonada']

# Generar item comida
variables_comida = []
cuadros_comida = []
texto_comida = []

i = 0
for comida in lista_comidas:
    # Crear los checkbutton
    variables_comida.append('')
    variables_comida[i] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[i],
                         command=revisar_check)
    comida.grid(row=i, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[i] = StringVar()
    texto_comida[i].set('0')
    cuadros_comida[i] = Entry(panel_comidas,
                              font=('Dosis', 14),
                              width=6,
                              state=DISABLED,
                              textvariable=texto_comida[i])
    cuadros_comida[i].grid(row=i,
                           column=1)

    i += 1

# Generar item bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

i = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[i] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[i],
                         command=revisar_check)
    bebida.grid(row=i, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[i] = StringVar()
    texto_bebida[i].set('0')
    cuadros_bebida[i] = Entry(panel_bebidas,
                              font=('Dosis', 14),
                              width=6,
                              state=DISABLED,
                              textvariable=texto_bebida[i])
    cuadros_bebida[i].grid(row=i,
                           column=1)

    i += 1

# Generar item postres
variables_postre = []
cuadros_postre = []
texto_postre = []

i = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[i] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 14),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[i],
                         command=revisar_check)
    postre.grid(row=i, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[i] = StringVar()
    texto_postre[i].set('0')
    cuadros_postre[i] = Entry(panel_postres,
                              font=('Dosis', 14),
                              width=6,
                              state=DISABLED,
                              textvariable=texto_postre[i])
    cuadros_postre[i].grid(row=i,
                           column=1)

    i += 1

# Variables comida
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 14, 'bold'),
                              bg='darkgrey',
                              fg='black')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 16),
                           bd=0,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 14, 'bold'),
                              bg='darkgrey',
                              fg='black')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 16),
                           bd=0,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 14, 'bold'),
                              bg='darkgrey',
                              fg='black')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 16),
                           bd=0,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 14, 'bold'),
                          bg='darkgrey',
                          fg='black')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 16),
                       bd=0,
                       width=10,
                       state='readonly',
                       textvariable=var_costo_postre)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                           text='Impuestos',
                           font=('Dosis', 14, 'bold'),
                           bg='darkgrey',
                           fg='black')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 16),
                        bd=0,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_postre)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Dosis', 14, 'bold'),
                       bg='darkgrey',
                       fg='black')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 16),
                    bd=0,
                    width=10,
                    state='readonly',
                    textvariable=var_costo_postre)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='black',
                   bg='darkgrey',
                   bd=0,
                   width=9)

    boton.grid(row=0, column=columnas)
    botones_creados.append(boton)
    columnas += 1

botones_creados[0].config(command=total)

# Área recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold',),
                    bd=1,
                    width=52,
                    height=10,
                    pady=34)
texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=45,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']

botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 15, 'bold'),
                   fg='black',
                   bg='white',
                   width=8)

    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la ventana se cierre
aplicacion.mainloop()
