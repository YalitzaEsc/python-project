import tkinter
from tkinter import ttk
from tkinter import messagebox


def guardar_datos():
    # Términos y condiciones
    terminos = terminos_aceptados.get()

    if terminos == "Aceptados":

        # Información usuario
        nombres = nombres_entrada.get()
        apellidos = apellidos_entrada.get()

        if nombres and apellidos:
            titulo_p = titulo_menu_desplegable.get()
            edad = edad_contador.get()
            nacionalidad = nacionalidad_menu_desplegable.get()

            print(f"Nombre(s): {nombres}\nApellido(s): {apellidos}")
            print(f"Título: {titulo_p}\nEdad: {edad} años")
            print(f"Nacionalidad: {nacionalidad}")

            # Información cursos
            estado_registro = registro_check_estado.get()
            numero_cursos = numero_cursos_contador.get()
            numero_semestres = numero_semestres_contador.get()

            print(f"Estatus: {estado_registro}")
            print(f"No. de cursos completados: {numero_cursos}")
            print(f"No. De semestres: {numero_semestres}")
            print("_" * 30, "\n")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Nombre y apellido necesarios.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="Por favor, acepta los términos y condiciones.")


ventana = tkinter.Tk()
ventana.title("Data Entry Form")

pantalla = tkinter.Frame(ventana)
pantalla.pack()

# Información de usuario
seccion_informacion_usuario = tkinter.LabelFrame(pantalla, text="Información de Usuario")
seccion_informacion_usuario.grid(row=0, column=0, padx=20, pady=10)

etiqueta_nombres = tkinter.Label(seccion_informacion_usuario, text="Nombre(s)")
etiqueta_nombres.grid(row=0, column=0)
etiqueta_apellidos = tkinter.Label(seccion_informacion_usuario, text="Apellido(s)")
etiqueta_apellidos.grid(row=0, column=1)

nombres_entrada = tkinter.Entry(seccion_informacion_usuario)
nombres_entrada.grid(row=1, column=0)
apellidos_entrada = tkinter.Entry(seccion_informacion_usuario)
apellidos_entrada.grid(row=1, column=1)

titulo = tkinter.Label(seccion_informacion_usuario, text="Título")
titulo.grid(row=0, column=2)
titulo_menu_desplegable = ttk.Combobox(seccion_informacion_usuario, values=["", "Doctor/a", "Licenciado/a", "Ingeniero(a)", "Estudiante"])
titulo_menu_desplegable.grid(row=1, column=2)

etiqueta_edad = tkinter.Label(seccion_informacion_usuario, text="Edad")
etiqueta_edad.grid(row=2, column=0)
edad_contador = tkinter.Spinbox(seccion_informacion_usuario, from_=18, to=100)
edad_contador.grid(row=3, column=0)

etiqueta_nacionalidad = tkinter.Label(seccion_informacion_usuario, text="Nacionalidad")
etiqueta_nacionalidad.grid(row=2, column=1)
nacionalidad_menu_desplegable = ttk.Combobox(seccion_informacion_usuario, values=["Estados Unidos", "México", "Perú", "Argentina", "España"])
nacionalidad_menu_desplegable.grid(row=3, column=1)

# Para que todos los widgets tengan espacios iguales
for widget in seccion_informacion_usuario.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Sección de curso
seccion_curso = tkinter.LabelFrame(pantalla)
seccion_curso.grid(row=1, column=0, sticky="news", padx=20, pady=10)

etiqueta_registro = tkinter.Label(seccion_curso, text="Estado de Registro")
etiqueta_registro.grid(row=0, column=0)

registro_check_estado = tkinter.StringVar(value="No registrado.") # Valor por default
registro_check = tkinter.Checkbutton(seccion_curso, text="Actualmente Registrado",
                                     variable=registro_check_estado, onvalue="Registrado", offvalue="No registrado")
registro_check.grid(row=1, column=0)

etiqueta_numero_cursos = tkinter.Label(seccion_curso, text="No. Cursos Completados")
etiqueta_numero_cursos.grid(row=0, column=1)
numero_cursos_contador = tkinter.Spinbox(seccion_curso, from_=0, to=200)
numero_cursos_contador.grid(row=1, column=1)

etiqueta_numero_semestres = tkinter.Label(seccion_curso, text="No. De Semestres")
etiqueta_numero_semestres.grid(row=0, column=2)
numero_semestres_contador = tkinter.Spinbox(seccion_curso, from_=0, to=100)
numero_semestres_contador.grid(row=1, column=2)

for widget in seccion_curso.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Términos y condiciones
seccion_terminos = tkinter.LabelFrame(pantalla, text="Términos y condiciones")
seccion_terminos.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terminos_aceptados = tkinter.StringVar(value="No aceptados")
terminos_check = tkinter.Checkbutton(seccion_terminos, text="He leído los términos y condiciones.",
                                     variable=terminos_aceptados, onvalue="Aceptados",
                                     offvalue="No aceptados")
terminos_check.grid(row=0, column=0)


# Botón
boton = tkinter.Button(pantalla, text="Ingresar Datos", command=guardar_datos)
boton.grid(row=3, column=0, padx=20, pady=10)


ventana.mainloop()
