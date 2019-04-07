

def sumar(num1, num2):
	sum = num1+num2
	return sum
	
def multiplicar(num1, num2):
	return num1*num2
	
def dividir(num1, num2):
	try: 
		div = num1/num2
		return div
	except Exception as e:
		print("Error trying to operate: ", e)
		return 0

def power(num1, num2):
	return num1**num2

	
def salida(opcion):
	if opcion == 1:
		suma = sumar(num1, num2)
		ans["suma"] = suma
		print(suma)
	elif opcion == 2:
		mult = multiplicar(num1,num2)
		ans["multiplicacion"] = mult
		print(mult)
	elif opcion == 3:
		div = dividir(num1, num2)
		ans["division"] = div
		print(div)
	elif opcion == 4:
		exp = power(num1,num2)
		ans["exponente"] = exp
		print(exp)
	elif opcion == 5:
		pass
	elif opcion == 0:
		print("Bye!")
		print(ans)
	else:
		print("Not able to process the instruction")
ans = {}
opcion = 2

while(opcion != 0):
	
	num1 = int(input("Introduzca numero 1: "))
	num2 = int(input("Introduzca numero 2: "))

	opcion = int(input("Escriba opcion: \n [0] Salir \n \n [1] Suma \n [2] Multiplicación \n [3] División \n [4] Exponencial \n"))
	salida(opcion)
	opcion = int(input("Para continuar pulse 5, para salir, pulse 0"))
	salida(opcion)


	
		
