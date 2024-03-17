import customtkinter as ctk


def add_tasks():
    tarea = entrada.get()
    label = ctk.CTkLabel(cuadro_con_barra_deslizadora, text=tarea)
    label.pack()
    entrada.delete(0, ctk.END)


ventana = ctk.CTk()
ventana.title('Prueba')
ventana.geometry('750x450')


etiqueta_titulo = ctk.CTkLabel(ventana, text='Daily Tasks', font=ctk.CTkFont(size=30, weight='bold'))
etiqueta_titulo.pack(padx=10, pady=(40, 20))


cuadro_con_barra_deslizadora = ctk.CTkScrollableFrame(ventana, width=500, height=280)
cuadro_con_barra_deslizadora.pack()


entrada = ctk.CTkEntry(cuadro_con_barra_deslizadora, width=400, placeholder_text='Add your tasks to do')
entrada.pack()


boton = ctk.CTkButton(ventana, text='Add', width=520, command=add_tasks)
boton.pack(pady=15)


ventana.mainloop()


















