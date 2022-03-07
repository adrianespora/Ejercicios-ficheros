archivo = '/Users/carol_000/Documents/Python/Ejercicios/08 - Ficheros/Ejercicio 08/calificaciones.csv'
def calificaciones(archivo):
    with open(archivo, 'r', encoding='utf-8')as fichero:
        notas = fichero.readlines()
        alumnos = []
        dicc_alumnos = {}
        titulo = notas[0]
        titulo = titulo.split(';')
        
        y = 0
        for x in notas[1:]:
            alumnos.append(x)
            for alumno in alumnos:
                alumno = alumno.split(';')
                n = 0
                for y in alumno:
                    dicc_alumnos[titulo[n]] = y
                    n += 1
            print(alumno)
        
        print(f'{titulo[0]}\n')
        print(f'{dicc_alumnos}')
        

calificaciones(archivo)