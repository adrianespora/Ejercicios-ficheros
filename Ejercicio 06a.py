'''Ejercicio 6
Escribir un programa para gestionar una agenda telefónica con los nombres 
y los teléfonos de los clientes de una empresa. El programa incorporar 
funciones crear el fichero con la agenda si no existe, para consultar 
el teléfono de un cliente, añadir el teléfono de un nuevo cliente y 
eliminar el teléfono de un cliente. 

La agenda debe estar guardada en 
el fichero de texto agenda.txt donde el nombre del cliente y su teléfono 
deben aparecer separados por comas y cada cliente en una línea distinta.'''


from argparse import ArgumentDefaultsHelpFormatter
from base64 import encode
from pickle import TRUE



def crear_contacto(nombre,cel):
    try:
        with open('./agenda2.txt', 'a' , encoding = 'utf-8') as agenda:
            agenda.write(f'\n{nombre},{cel}')
    except:
        print("hay un errror en crear contacto")

def consulta_telefono(nombre):
    try:
        with open('./agenda2.txt','r', encoding= 'utf-8') as agenda:
            cuenta = 0
            for linea in agenda.readlines():
                if linea == '\n':
                    continue
                else:
                    linea = linea.split(',')
                    if linea[0] == nombre:
                        print(f'El telefono de {nombre} es: {linea[1]}')
                        cuenta += 1
            if cuenta == 0:
                print("Ese contacto no existe")
    except:
        print("hay un error en consulta telefono")

def eliminar_contacto(nombre):
    try:
        with open('./agenda2.txt','r',encoding='utf-8') as agenda:
            directorio = agenda.readlines()
            dicc_directorio = {}
            for contacto in directorio:
                if contacto == '\n':
                    continue
                else:
                    datos= contacto.split(',')
                    dicc_directorio[datos[0]] = datos[1]
            if nombre in dicc_directorio.keys():
                del dicc_directorio[nombre]
            else:
                print("No existe contacto para elimiar")
        with open('./agenda2.txt','w', encoding= 'utf-8') as agenda:
            for nombre, telefono in dicc_directorio.items():
               agenda.write(f'{nombre},{telefono}')
    except:
        print("hay un error en elimiar contacto")

def menu():
    while TRUE:
        print("""Menu agenda telefonica\n\n
        1- Consultar telefono\n
        2- Agregar telefono\n
        3- Eliminar un telefono\n
        4- Salir\n
        """)
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            consulta_telefono(nombre)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del cliente: ")
            cel = input("Ingrese el telefono del cliente: ")
            crear_contacto(nombre, cel)
        elif opcion == 3:
            nombre = input("Ingrese el nombre del cliente que quiere borrar: ")
            eliminar_contacto(nombre)
        elif opcion == 4:
            break
    return

menu()