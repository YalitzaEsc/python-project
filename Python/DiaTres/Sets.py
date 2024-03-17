mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))

otro_set = {1, 2, 3, 4, (3, 9, 4)}
print(type(otro_set))
print(len(otro_set))
print(9 in otro_set)

s1 = {1,2,3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
s1.remove(3)
eliminado = s1.pop()
print(s1)

s2.clear()
print(s2)

