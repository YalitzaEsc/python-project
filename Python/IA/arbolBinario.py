class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.vacio():
            self.raiz = Nodo(valor)
        else:
            self.insertarNodo(valor, self.raiz)

    def insertarNodo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.insertarNodo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.insertarNodo(valor, nodo_actual.derecha)

    def imprimirArbol(self):
        self.imprimir(self.raiz)

    def imprimir(self, nodo_actual):
        if nodo_actual is not None:
            self.imprimir(nodo_actual.izquierda)
            print(nodo_actual.valor, " ")
            self.imprimir(nodo_actual.derecha)


# Prueba
arbol = ArbolBinario()
print(arbol.vacio())
arbol.insertar(5)
arbol.insertar(10)
arbol.insertar(12)
arbol.insertar(3)
arbol.insertar(1)
arbol.imprimirArbol()
