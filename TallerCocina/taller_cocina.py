
def calcular_mejor_opcion( M , p ):
    resultado = encontrar_mejor_opcion_matriz( M )
    ingredientes = []
    if resultado["discordancia"] > p:
        # no caben dos, podria ser cualquiera indivual solamente
        return []
    ingredientes.append( resultado["i"] )
    ingredientes.append( resultado["j"] )
    resultado = obtener_siguiente_ingrediente( ingredientes , M , p,  resultado["discordancia"] )
    return resultado

def obtener_siguiente_ingrediente( ingredientes , M , p, discordanciaAcum ):
    # el valor agregando los ingredientes y retornar
    ingredientesUsados = len( ingredientes )
    nuevoaAcum = [ 0.0 ] * len( M ) 
    menor = 9999999999.0 # inicializar en un numero muy grande

    while discordanciaAcum <= p and ingredientesUsados <= len( M ):
        menor = 9999999999.0 
        entra = False
        for i in range( len( M ) ):
            if i not in ingredientes:
                for j in ingredientes:
                    nuevoaAcum[i] = nuevoaAcum[i] + M[j][i]                   
                nuevoaAcum[i] = nuevoaAcum[i] + discordanciaAcum
        
        for ingrediente in range( len( nuevoaAcum ) ):
            if nuevoaAcum[ingrediente] < menor and ingrediente not in ingredientes:
                menor = nuevoaAcum[ingrediente]
                nuevoIngrediente = ingrediente
                entra = True

        if entra and nuevoaAcum[nuevoIngrediente]  <= p:
            ingredientes.append( nuevoIngrediente )
            discordanciaAcum = nuevoaAcum[nuevoIngrediente] 
            ingredientesUsados = len( ingredientes )    
        else :
            return { "ingredientes" : ingredientes , "discordancia" : discordanciaAcum }    
        nuevoaAcum = [ 0.0 ] * len( M ) 
    return { "ingredientes" : ingredientes , "discordancia" : discordanciaAcum }           

                     
        

def encontrar_mejor_opcion_matriz( M ):
    i_seleccionado , j_seleccionado = -1 , 1
    menor = 9999999999.0 # inicializar en un numero muy grande
    for i in range( len( M ) ):
        for j in range( len( M ) ):
            if i != j:
                if M[ i ][ j ] < menor:
                    menor = M[ i ][ j ]
                    i_seleccionado = i
                    j_seleccionado = j
    return { "i" : i_seleccionado , "j": j_seleccionado , "discordancia" : menor } 

def main():
    M = [\
        [ 0.0 , 0.4 , 0.2 , 0.9 , 1.0 ],\
        [ 0.4 , 0.0 , 0.1 , 1.0 , 0.2 ],\
        [ 0.2 , 0.1 , 0.0 , 0.8 , 0.5 ],\
        [ 0.9 , 1.0 , 0.8 , 0.0 , 0.2 ],\
        [ 1.0 , 0.2 , 0.5 , 0.2 , 0.0 ],\
        ]
    print calcular_mejor_opcion( M , 2.0 )


if __name__ == "__main__":
    main()
