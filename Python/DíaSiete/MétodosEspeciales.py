class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Álbum: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        return f"Se ha eliminado el álbum {self.titulo}."



mi_cd = CD('Imagine Dragons', 'Evolve', 12)
print(mi_cd)
print(len(mi_cd))























