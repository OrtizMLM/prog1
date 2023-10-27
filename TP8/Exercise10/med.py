def medidas_hoja_A(N):
    if N == 0:
        return(841, 1189)
    else:
        ancho_anterior, largo_anterior = medidas_hoja_A(N - 1)
        
        # Calculamos las dimensiones de la hoja A(N) doblando a la mitad las dimensiones de A(N-1)
        ancho_actual = largo_anterior // 2
        largo_actual = ancho_anterior
        
        # Retornamos las dimensiones de la hoja A(N) en una tupla
        return (ancho_actual, largo_actual)
    