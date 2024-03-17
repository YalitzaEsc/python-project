import mysql.connector
import tkinter
from tkinter import *
from tkmacosx import Button


base_datos = ''


def salir():
    exit()


def conectar():
    global ventana_elegir_opcion
    global base_datos

    host_name = host_entrada.get()
    usuario = usuario_entrada.get()
    contraseña = contraseña_entrada.get()
    puerto = puerto_entrada.get()
    nombre_base_datos = base_Datos_entrada.get()

    try:
        base_datos = mysql.connector.connect(host=host_name, user=usuario, password=contraseña,
                                             port=puerto, database=nombre_base_datos)

    except:
        tkinter.messagebox.showwarning(title="Error de conexión",
                                       message="Ha ocurrido un error, revisa los datos ingresados e inténtalo de nuevo.")
    else:
        tkinter.messagebox.showwarning(title="Conexión exitosa",
                                       message="¡La base de datos se ha conectado exitosamente!")
        ventana.destroy()
        ventana_dos = tkinter.Tk()


ventana = tkinter.Tk()
ventana.geometry = ('800x500')
ventana.title("Iniciar sesión")
imagen = PhotoImage(file='icono.png')

pantalla = tkinter.Frame(ventana)
pantalla.pack()

seccion_logo = tkinter.Frame(pantalla)
seccion_logo.grid(row=0, column=0, padx=20, pady=10)
etiqueta_logo = Label(seccion_logo, image=imagen)
etiqueta_logo.pack()


seccion_iniciar_sesion = tkinter.Frame(pantalla)
seccion_iniciar_sesion.grid(row=0, column=1, padx=20, pady=10)
etiqueta_iniciar_sesion = tkinter.Label(seccion_iniciar_sesion, text="Ingresa a tu base de datos", font=('Times New Roman', 30))
etiqueta_iniciar_sesion.grid(row=0, column=0, padx=20, pady=10)

etiqueta_host = tkinter.Label(seccion_iniciar_sesion, text="Host", font=('Times New Roman', 14))
etiqueta_host.grid(row=1, column=0, sticky='w')
host_entrada = tkinter.Entry(seccion_iniciar_sesion)
host_entrada.grid(row=2, column=0, sticky='news')

etiqueta_usuario = tkinter.Label(seccion_iniciar_sesion, text="Usuario", font=('Times New Roman', 14))
etiqueta_usuario.grid(row=3, column=0, sticky='w')
usuario_entrada = tkinter.Entry(seccion_iniciar_sesion)
usuario_entrada.grid(row=4, column=0, sticky='news')

etiqueta_contraseña = tkinter.Label(seccion_iniciar_sesion, text="Contraseña", font=('Times New Roman', 14))
etiqueta_contraseña.grid(row=5, column=0, sticky='w')
contraseña_entrada = tkinter.Entry(seccion_iniciar_sesion, show="*")
contraseña_entrada.grid(row=6, column=0, sticky='news')

etiqueta_puerto = tkinter.Label(seccion_iniciar_sesion, text="Puerto", font=('Times New Roman', 14))
etiqueta_puerto.grid(row=7, column=0, sticky='w')
puerto_entrada = tkinter.Entry(seccion_iniciar_sesion)
puerto_entrada.grid(row=8, column=0, sticky='news')

etiqueta_base_Datos = tkinter.Label(seccion_iniciar_sesion, text="Base de datos", font=('Times New Roman', 14))
etiqueta_base_Datos.grid(row=9, column=0, sticky='w')
base_Datos_entrada = tkinter.Entry(seccion_iniciar_sesion)
base_Datos_entrada.grid(row=10, column=0, sticky='news')

boton_ingresar = Button(pantalla, text="Conectar", bg='#ffe6ba', fg='black', command=conectar)
boton_ingresar.grid(row=11, column=1, padx=20, pady=10)



ventana.mainloop()
