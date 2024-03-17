mi_tuple = (1, 2, 3, 4)
mi_tuple_dos = 'rosa', 2, 5, 'verde', mi_tuple

print(mi_tuple[0])
print(mi_tuple[-2])
print(mi_tuple_dos[4])
print(mi_tuple_dos[4][1])

mi_tuple_dos = list(mi_tuple_dos)
print(type(mi_tuple_dos))

t = (1, 2, 3)
x, y, z = t
print(t)
print(x, y, z)

print(t.count(1))
print(t.index(2))
