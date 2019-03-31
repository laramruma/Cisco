nombres = ["Juan", "Luisa", "Pedro", "Carmen", "Irene"]
selected = []

for i in nombres:
	print("Se llama: ", i)
	if "a" in i:
		selected.append(i)

print(selected)