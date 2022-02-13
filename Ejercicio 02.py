'''Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10,
 lea el fichero tabla-n.txt con la tabla de multiplicar de
 ese número, donde n es el número introducido, y la muestre
  por pantalla. Si el fichero no existe debe mostrar un
   mensaje por pantalla informando de ello.'''

def elegirtabla():
    numero = int(input("Ingrese un numero entero entre 1 y 10: "))
    ubicacion = (f"/Users/Carol_000/Documents/Python/ejercicios/08 - ficheros/tabla-{numero}.txt")
    try:
        with open(f"{ubicacion}",'r') as archivo1:
            print(archivo1.read())
    except FileNotFoundError as eror:
        print("El archivo no existe")


elegirtabla()
