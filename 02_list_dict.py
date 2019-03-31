list_str = ["Hola", "Mundo", "Aqui", "mi", "primer", "programa"]
list_int = [1,2,3,4,5,6,7,8,9,0]
list_var = ["Hola", 1, "Mundo", 3.9]
print(list_str, list_int, list_var, sep="\n->")
last_str = list_str[-1]
last_int = list_int[-1]
last_var = list_var[-1]

print(last_str, last_int, last_var, sep=",")

print("Aqui la información de las listas: ", list_str, "Ahora con enteros: ", list_int, "Ahora con todo: ", list_var, sep="\n")


catalogo = {'diney': 'frozen', 'dreamworks': 'brave', 'pixar':'toy story 3'}
print(catalogo)

for key in catalogo.keys():
	print(key, "->", catalogo[key])
	
print("Ahora solo las claves")
for key in catalogo.keys():
	print(key)

print("Ahora solo los valores")
for values in catalogo.values():
	print(values)