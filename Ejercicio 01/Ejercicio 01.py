'''Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde
 en un fichero con el nombre tabla-n.txt la tabla de multiplicar
 de ese número, done n es el número introducido.'''

def numero(entero):
    numero = entero
    nombrearchivo = "tabla-" + str(entero)
    if numero != 0:
        i = 1
        while i <= 10:
            with open(f"/Users/Carol_000/Documents/Python/ejercicios/08 - ficheros/{nombrearchivo}.txt",'a') as archivo1:
                archivo1.write(f"{numero} x {i} = {numero*i}\n")
                i += 1

numero(4)
