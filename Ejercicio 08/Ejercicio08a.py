ruta = '/Users/carol_000/Documents/Python/Ejercicios/08 - Ficheros/Ejercicio 08/calificaciones.csv'
def calificaciones(ruta):
    with open(ruta, 'r', encoding='utf-8')as fichero:
        archivo = fichero.readlines()
        claves = archivo[0]
        claves = claves[:-1].split(';')
        alumnos = []
        datos = []
        for alumno in archivo[1:]:
            datos = alumno[:-1].split(';')
            estudiante = {}
            for n in range(len(datos)):
                estudiante[claves[n]] = datos[n]
            alumnos.append(estudiante)

        return calificaciones

"""Una función que reciba una lista de diccionarios como la que devuelve 
la función anterior y añada a cada diccionario un nuevo par con la nota
 final del curso. El peso de cada parcial de teoría en la nota final es
  de un 30% mientras que el peso del examen de prácticas es de un 40%."""

def nota_final(nombre):
    with open(ruta, 'a', encoding='utf-8') as fichero:
        archivo = fichero.readlines()
        claves = archivo[0]
        claves = claves[:-1].split(';')
        clavesAll = claves
        agregar = ['Final1','Final2', 'FinalPracticas', 'NotaFinal']
        clavesAll= clavesAll + agregar
        print(clavesAll)
        for alumno in archivo[1:]:
            datos = alumno[:-1].split(';')
            if datos[3] > 4:
                print(datos[3])

              


calificaciones(ruta)
nota_final(calificaciones)