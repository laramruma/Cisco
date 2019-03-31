num = int(input("Introducir número: "))
if num < 20:
	print("Número ", num, "menor que 20")
elif num > 20 and num < 39:
	print("Número ", num, "entre 20 y 39")	
elif num > 40 and num < 60:
	print("Número ", num, "entre 40 y 59")
elif num > 60:
	print("Número ", num, "mayor que 60")
else:
	print("pues hay un errorcillo")