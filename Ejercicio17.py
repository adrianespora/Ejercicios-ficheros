class RomanNumerals:

    def to_roman(val):
        cadena = []
        numero_en_cadena = str(val)
        unidades = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
        decenas = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'Xl', 5:'L', 6:'LX', 7:'LXX',8:'LXXX',9:'XC' }
        centenas = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DX', 7:'DXX',8:'DXXX',9:'CM' }
        miles = {1:'M', 2:'MM', 3:'MMM'}

        if val > 0 and val <= 10:
            cadena.append(unidades[val])

        if len(numero_en_cadena) == 2 and val > 10:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[0])])

        if len(numero_en_cadena) == 3:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[1])])
            cadena.append(centenas[int(numero_en_cadena[0])])

        if len(numero_en_cadena) == 4:
            cadena.append(unidades[int(numero_en_cadena[-1])])
            cadena.append(decenas[int(numero_en_cadena[2])])
            cadena.append(centenas[int(numero_en_cadena[1])])
            cadena.append(miles[int(numero_en_cadena[0])])

        cadena.reverse() # invierto el orden de la lista
        resultado = ''.join(cadena) # convierto la lista en cadena

        print(resultado)
               
    

RomanNumerals.to_roman(2158)


"""
(1000), 'M', '1000 should == "M"')
(4), 'IV', '4 should == "IV"')
(1), 'I', '1 should == "I"')
(1990), 'MCMXC', '1990 should == "MCMXC"')
(2008), 'MMVIII', '2008 should == "MMVIII"')
"""