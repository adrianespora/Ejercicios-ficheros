'''Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante
su url y muestre por pantalla el número de palabras que contiene.'''

def palabrasarchivo(url):
    from urllib import request
    from urllib.error import URLError
    try:
        archivo = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = archivo.read()
        return len(content.split())

print(palabrasarchivo('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(palabrasarchivo('https://no-existe.txt'))
