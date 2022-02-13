with open('./agenda3.txt','r', encoding= 'utf-8') as agenda:
    nombre = 'adri'
    telefono = 123
    directorio = agenda.readlines()
    diccionario_directorio = {}
    for contacto in directorio:
        datos = contacto.split(',')
        diccionario_directorio[datos[0]] = datos[1]
    print(diccionario_directorio)
    if nombre in diccionario_directorio.keys():
        del diccionario_directorio[nombre]
    print(diccionario_directorio)
    with open('./agenda3.txt','w', encoding= 'utf-8') as agenda:
        for nombre, telefono in diccionario_directorio.items():
            agenda.write(f'{nombre},{telefono}\n')
