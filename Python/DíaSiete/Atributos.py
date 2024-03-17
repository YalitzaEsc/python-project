class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('Negro', 'ciervo')

print(f"Mi pájaro es un {mi_pajaro.especie} y es de "
      f"color {mi_pajaro.color}.")
print(Pajaro.alas)
print(mi_pajaro.alas)
