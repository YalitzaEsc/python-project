diccionario = {"c1":"valor1", "c2":"valor2"}
print(diccionario)

resultado = diccionario["c1"]
print(resultado)

cliente = {'nombre':'Claudia', 'apellido':'Escárcega', 'peso':44, 'altura':1.60}
print((cliente['apellido']))
print((cliente['altura']))

lista = ["rojo", "azul"]
diccionario_dos = {'c1': [10, 20, 30], 'c2': {'s1':100, 's2': 200}, 'c3': lista}
print(diccionario_dos)
print(diccionario_dos['c1'][1])
print(diccionario_dos['c2']['s2'])

dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic_dos = {1: 'a', 2: 'b'}
dic_dos[3] = 'c'
print(dic_dos)

dic_dos[2] = 'B'
print(dic_dos)
print(dic.keys())
print(dic.values())
print(dic.items())
