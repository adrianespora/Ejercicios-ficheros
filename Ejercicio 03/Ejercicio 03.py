'''Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10
, lea el fichero tabla-n.txt con la tabla de multiplicar de
ese número, y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla
informando de ello.'''

def multiplicar(n,m):
    n = int(input("Ingrese un numero entre 1 y 10: "))
    m = int(input("Ingrese otro numero entre 1 y 10: "))
    ubicacion = (f"/Users/Carol_000/Documents/Python/ejercicios/08 - ficheros/tabla-{n}.txt")
    try:
        with open((ubicacion),'r') as archivo1:
            listaarchivo1 = archivo1.readlines() # para leer una linea en particular, creo una lista del archivo
            print(listaarchivo1[m-1]) # Utilizo la lista para ubicar la linea que quiero devolver
    except FileNotFoundError as error:
        print("No se encontro el archivo")
