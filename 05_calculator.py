num1 = int(input("Introduzca numero 1: "))
num2 = int(input("Introduzca numero 2: "))

def sumar(num1, num2):
	return num1+num2
	
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



opcion = int(input("Escriba opcion: \n [1] Suma \n [2] Multiplicación \n [3] División \n [4] Exponencial \n"))



if opcion == 1:
	suma = sumar(num1, num2)
	print(sum)
elif opcion == 2:
	mult = multiplicar(num1,num2)
	print(mult)
elif opcion == 3:
	div = dividir(num1, num2)
	print(div)
elif opcion == 4:
	exp = power(num1,num2)
	print(exp)
	
