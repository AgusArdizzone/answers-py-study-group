nucleotidos = ['A','C','G','U']
codon_principal = 'AUG' 
codones_final = ['UAA','UAG','UGA']
def hay_codones_oblig(cad):
    return (codon_principal in cad) and  bool([cod for cod in codones_final if cod in cad])

def detectar_secuencias(cadena):
    '''Detecta secuencias dentro del string.
       Devuelve la cantidad de secuencias detectadas.
    '''
    cont = 0
    if(not hay_codones_oblig(cadena)):
        return cont
    else:
        hay_secuencias = True
        while hay_secuencias:
            comienzo_sec = cadena.index('AUG')
            print('comienzo',comienzo_sec)
            pos_cod_final = [cadena.index(cod) for cod in codones_final if cod in cadena]
            print(pos_cod_final)
            fin_sec = min(pos_cod_final)
            print('fin',fin_sec)
            cadena = cadena.replace(cadena[0:(fin_sec+3)],'')
            cont+=1
            print(cadena)
            hay_secuencias = hay_codones_oblig(cadena)
        return cont
# cuando dos codones oblig estan unidos,los toma igual. EJ AUGA
# hay que arreglar eso viendo si el codon del comienzo y el del final estan en el mismo espacio

        
    
cadena = input("Ingrese secuencia:")
numsec = detectar_secuencias(cadena)
print("Secuencias detectadas: {}".format(numsec))
