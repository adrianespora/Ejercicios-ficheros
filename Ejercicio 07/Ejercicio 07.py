"""Ejercicio 7
El fichero cotizacion.csv contiene las cotizaciones de 
las empresas del IBEX35 con las siguientes columnas: 
Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa)
, Máximo (precio máximo de la acción durante la jornada),
 Mínimo (precio mínimo de la acción durante la jornada),
  Volumen (Volumen al cierre de bolsa),
   Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones 
y devuelva un diccionario con los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto 
por la función anterior y cree un fichero en formato csv 
con el mínimo, el máximo y la media de dada columna."""
import csv
from dataclasses import replace


ubicacion_archivo = "C:/Users/carol_000/Documents/Python/Ejercicios/08 - Ficheros/Ejercicio 07/cotizacionlimpia.csv"

with open(ubicacion_archivo, encoding='utf-8') as fichero:
        lector = csv.reader(fichero)
        diccionario_lector = {}
        filas = []
        columnaFinal = []
        columnaMaximo = []
        columnaMinimo = []
        columnaVolumen = []
        columnaEfectivo = []

        n = 0
        for fila in lector:
            filas = filas + fila
            diccionario_lector[n] = fila
            columnaFinal.append(diccionario_lector[n][1])
            columnaMaximo.append(diccionario_lector[n][2])
            columnaMinimo.append(diccionario_lector[n][3])
            columnaVolumen.append(diccionario_lector[n][4])
            columnaEfectivo.append(diccionario_lector[n][5])
            n += 1

        columnaFinal.pop(0) #quito el primer elemento para poder hacer los calculos
        columnaMaximo.pop(0) #quito el primer elemento para poder hacer los calculos
        columnaMinimo.pop(0) #quito el primer elemento para poder hacer los calculos
        columnaVolumen.pop(0) #quito el primer elemento para poder hacer los calculos
        columnaEfectivo.pop(0) #quito el primer elemento para poder hacer los calculos

        float_columnaFinal = list(map(float, columnaFinal)) #paso los numeros str a numeros
        float_columnaMaximo = list(map(float, columnaMaximo))
        float_columnaMinimo = list(map(float, columnaMinimo))
        float_columnaVolumen = list(map(float, columnaVolumen))
        float_columnaEfectivo = list(map(float, columnaEfectivo))

        min_columnaFinal = min(float_columnaFinal) #min columna final
        max_columnaFinal = max(float_columnaFinal) #max columna final
        prom_columnaFinal = round(sum(float_columnaFinal)/len(float_columnaFinal)) #promedio columna final
        
        min_columnaMaximo = min(float_columnaMaximo) #min columna final
        max_columnaMaximo = max(float_columnaMaximo) #max columna final
        prom_columnaMaximo = round(sum(float_columnaMaximo)/len(float_columnaMaximo)) #promedio columna final
        
        min_columnaMinimo = min(float_columnaMinimo) #min columna final
        max_columnaMinimo = max(float_columnaMinimo) #max columna final
        prom_columnaMinimo = round(sum(float_columnaMinimo)/len(float_columnaMinimo)) #promedio columna final
        
        min_columnaVolumen = min(float_columnaVolumen) #min columna final
        max_columnaVolumen = max(float_columnaVolumen) #max columna final
        prom_columnaVolumen = round(sum(float_columnaVolumen)/len(float_columnaVolumen)) #promedio columna final
        
        min_columnaEfectivo = min(float_columnaEfectivo) #min columna final
        max_columnaEfectivo = max(float_columnaEfectivo) #max columna final
        prom_columnaEfectivo = round(sum(float_columnaEfectivo)/len(float_columnaEfectivo)) #promedio columna final
        fila1 = 'Minimos'
        fila2 = 'Maximos'
        fila3 = 'Promedios'
        minimos = [fila1, min_columnaFinal,min_columnaMaximo,min_columnaMinimo,min_columnaVolumen,min_columnaEfectivo]
        maximos = [fila2,max_columnaFinal,max_columnaMaximo,max_columnaMinimo,max_columnaVolumen,max_columnaEfectivo]
        promedios = [fila3, prom_columnaFinal,prom_columnaMaximo,prom_columnaMinimo,prom_columnaVolumen,prom_columnaEfectivo]
        with open('C:/Users/carol_000/Documents/Python/Ejercicios/08 - Ficheros/Ejercicio 07/csvresumido.csv', 'w', encoding='utf-8') as archivo:
            writer = csv.writer(archivo, delimiter = ';')
            writer.writerow(diccionario_lector[0])
            writer.writerow(minimos)
            writer.writerow(maximos)
            writer.writerow(promedios)




