class RomanNumerals:

    def to_roman(val):
        cadena = []
        numero_en_cadena = str(val)
        unidades = {'1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX', '10':'X'}
        decenas = {'1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX','8':'LXXX','9':'XC' }
        centenas = {'1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC','8':'DCCC','9':'CM' }
        miles = {'1':'M', '2':'MM', '3':'MMM' }
        n = -1
        cadena_romano = []
        
        for x in numero_en_cadena:
            cadena.append(x)

        """ UNIDADES"""
        try:
            if cadena[n] in unidades:
                cadena_romano.append(unidades[cadena[n]])
                n -= 1
            elif cadena[n] == '0':
                n -=1
        except:
            pass

        """ DECENAS"""
        try:
            if cadena[n] in decenas:
                cadena_romano.append(decenas[cadena[n]])
                n -= 1
            elif cadena[n] == '0':
                n -=1
        except:
            pass

        """ CENTENAS"""
        try:
            if cadena[n] in centenas:
                cadena_romano.append(centenas[cadena[n]])
                n -= 1
            elif cadena[n] == '0':
                n -=1
        except:
            pass

        """ MILES"""
        try:
            if cadena[0] in miles:
                cadena_romano.append(miles[cadena[0]])
                
        except:
            pass
        cadena_romano.reverse() # invierto el orden de la lista
        resultado = ''.join(cadena_romano) # convierto la lista en cadena

        print(resultado)
               
    def from_roman(roman_num):
        cadena_romano = roman_num
        miles = 'M'
        n= 0
        cuenta_miles = 0
        cuenta_unidades = '0'
        """ MILES """
        if cadena_romano[n] == miles:
            while cadena_romano[n] == miles:
                cuenta_miles += 1
                n += 1
            
        
        elif cadena_romano[n] == 'C':
            cuenta_cientos +=1
            n +=1
            if cadena_romano[n] == 'C':
                cuenta_cientos +=1
                n +=1
                if cadena_romano[n] == 'C':
                    cuenta_cientos +=1
                    n +=1
            elif cadena_romano[n] == 'D':
                cuenta_cientos += 4
                n +=1
            elif cadena_romano[n] == 'M':
                cuenta_cientos +=8
                n +=1
        elif cadena_romano[n] == 'D':
            cuenta_cientos += 5
            n +=1
            if cadena_romano[n] == 'C':
                cuenta_cientos +=1
                n += 1
                if cadena_romano[n] == 'C':
                    cuenta_cientos +=1
                    n += 1
                    if cadena_romano[n] == 'C':
                        cuenta_cientos +=1
                        n += 1



        cuenta_decenas = 0
                        
        if cadena_romano[n] == 'X': ## 10
            cuenta_decenas += 1
            n += 1
            if cadena_romano[n] == 'X': ## 20
                cuenta_decenas += 1
                n += 1
                if cadena_romano[n] == 'X': #30
                    cuenta_decenas += 1
                    n += 1
            elif cadena_romano[n] == 'L': #40
                cuenta_decenas += 3
                n += 1
            elif cadena_romano[n] == 'C': #90
                cuenta_decenas += 8
                n += 1
            
        elif cadena_romano[n] == 'L':
            cuenta_decenas += 5
            n +=1
            if cadena_romano[n] == 'X':
                cuenta_decenas +=1
                n += 1
                if cadena_romano[n] == 'X':
                    cuenta_decenas +=1
                    n += 1
                    if cadena_romano[n] == 'X':
                        cuenta_decenas +=1
                        n += 1


            print(cuenta_miles) 
            print(cuenta_cientos)
            print(cuenta_decenas)
            print(cuenta_unidades)
       
   

RomanNumerals.to_roman('2008')
RomanNumerals.from_roman('MMVIII')
RomanNumerals.to_roman('1990')
RomanNumerals.from_roman('MCMXC')
RomanNumerals.to_roman('1940')
RomanNumerals.from_roman('MCMXL')
RomanNumerals.to_roman('1930')
RomanNumerals.from_roman('MCMX')
RomanNumerals.to_roman('1950')
RomanNumerals.from_roman('MCMLV')
RomanNumerals.to_roman('1970')
RomanNumerals.from_roman('MCMLXXV')

"""
(1000), 'M', '1000 should == "M"')
(4), 'IV', '4 should == "IV"')
(1), 'I', '1 should == "I"')
(1990), 'MCMXC', '1990 should == "MCMXC"')
(2008), 'MMVIII', '2008 should == "MMVIII"')
"""