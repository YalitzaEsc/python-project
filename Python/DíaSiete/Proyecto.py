from os import system
from colorama import Fore


def crear_cliente():
    print(Fore.LIGHTWHITE_EX + "¡Bienvenido a su cajero automático!\n")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    system('clear')

    return nombre, apellido


class Persona:
    nombre, apellido = crear_cliente()


class Cliente(Persona):
    def __init__(self, numero_cta, balance):
        self.numero_cta = numero_cta
        self.balance = balance

    def imprimir(self):
        print(f"Nombre del cliente: {cliente.nombre} {cliente.apellido}\n"
              f"No. de cuenta: {self.numero_cta}\n"
              f"Balance: ${self.balance}")

    def depositar(self, cantidad_deposito):
        self.balance += cantidad_deposito

    def retirar(self, cantidad_retiro):
        self.balance -= cantidad_retiro


cliente = Cliente(8923847, 5000)


def iniciar():
    print(f"Hola, {Persona.nombre}. ¿Qué operación desea realizar hoy?\n")

    salir = False
    opcion = 0

    while not salir:
        opcion = int(input("[1] Depositar dinero\n"
                           "[2] Retirar dinero\n"
                           "[3] Imprimir información\n"
                           "[4] Salir\n\n"
                           "Ingrese una opción del menú: "))
        system('clear')

        if opcion == 1:
            cantidad = int(input("Cantidad a depositar: "))
            cliente.depositar(cantidad)
            system('clear')
            print(f"\n¡Depósito realizado con éxito!\n"
                  f"Su saldo actual es ${cliente.balance}\n")

            regreso = int(input("[1] Volver al menú principal\n"
                                "[2] Salir\n\n"
                                "Ingrese una opción del menú: "))
            if regreso == 2:
                system('clear')
                print(Fore.RED + "Un gusto servirle.")
                exit()
            else:
                pass
            system('clear')

        if opcion == 2:
            cantidad = int(input("Cantidad a retirar: "))
            if cantidad > cliente.balance:
                cantidad = int(input(Fore.RED + "Fondos insuficientes, inténtelo con otra cantidad: "))

            cliente.retirar(cantidad)
            system('clear')
            print(Fore.LIGHTWHITE_EX + f"\n¡Retiro realizado con éxito!\n"
                    f"Su saldo actual es ${cliente.balance}\n")

            regreso = int(input("[1] Volver al menú principal\n"
                                "[2] Salir\n\n"
                                "Ingrese una opción del menú: "))
            if regreso == 2:
                system('clear')
                print(Fore.RED + "Un gusto servirle.")
                exit()
            else:
                pass
            system('clear')

        if opcion == 3:
            system('clear')
            cliente.imprimir()
            regreso = int(input("\n[1] Volver al menú principal\n"
                                "[2] Salir\n\n"
                                "Ingrese una opción del menú: "))
            if regreso == 2:
                system('clear')
                print(Fore.RED + "Un gusto servirle.")
                exit()
            else:
                pass
            system('clear')

        if opcion == 4:
            print(Fore.RED + "Un gusto servirle.")
            salir = True
        if opcion > 4:
            system('clear')
            print(Fore.RED + "Elija una opción correcta\n")
            system('clear')


iniciar()
