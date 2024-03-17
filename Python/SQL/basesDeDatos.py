import mysql.connector

base_datos = ''


def conectar():
    global base_datos

    try:
        base_datos = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Y98490133y',
            port='3306',
            database='python')
    except:
        print("Error")
    else:
        mycursor = base_datos.cursor()
        mycursor.execute('SELECT * FROM users')  # Selecciona la tabla
        usuarios = mycursor.fetchall()  # Regresa la tabla en forma de tuple

        for usuario in usuarios:
            print(usuario)
            print("\nID: ", usuario[0], "\nNombre de usuario: ", usuario[1], "\nContraseña: ", usuario[2], "\n")


conectar()
