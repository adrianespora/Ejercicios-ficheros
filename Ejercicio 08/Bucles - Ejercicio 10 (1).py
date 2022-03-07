n = int(input("Ingrese un numero entero mayor que 1: "))
i = 2
while n%i !=0:
	i = i+1
if i == n:
	print("El numero ingresado un numero primo")
else:
	print("El numero ingresado no es un numero primo")