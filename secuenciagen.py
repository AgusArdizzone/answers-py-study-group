nucleotidos = ['A','C','G','U']
codon_principal = 'AUG' 
codones_final = ['UAA','UAG','UGA']

def detectar_secuencias(cadena):
    '''Detecta secuencias dentro del string.
       Devuelve la cantidad de secuencias detectadas.
    '''
    lista_secuencias = [codon_principal+sec for sec in cadena.split(codon_principal) if sec[-3:] in codones_final]
    return len(lista_secuencias)
        
    
cadena = input("Ingrese secuencia:")
numsec = detectar_secuencias(cadena)
print("Secuencias detectadas: {}".format(numsec))
