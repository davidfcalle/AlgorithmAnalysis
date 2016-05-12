
def calcular_mejor_opcion( M , p ):
    resultado = encontrar_mejor_opcion_matriz( M )
    ingredientes = []
    if resultado["discordancia"] > p:
        # no caben dos, podria ser cualquiera indivual solamente
        return []
    ingredientes.append( resultado["i"] )
    ingredientes.append( resultado["j"] )
    ingrendientes = obtener_siguiente_ingrediente( ingredientes , M , P )
    return ingredientes

def obtener_siguiente_ingrediente( ingredientes , M , p ):
    # el valor agregando los ingredientes y retornar

def encontrar_mejor_opcion_matriz( M ):
    i_seleccionado , j_seleccionado = -1 , 1
    menor = 99999.0 # inicializar en un numero muy grande
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
        [ 0.4 , 0.0 , 0.1 , 1.0 , 1.2 ],\
        [ 0.2 , 0.1 , 0.0 , 0.8 , 0.5 ],\
        [ 0.9 , 1.0 , 0.8 , 0.0 , 0.2 ],\
        [ 1.0 , 0.2 , 0.5 , 0.2 , 0.0 ],\
        ]
    calcular_mejor_opcion( M , 2.0 )

if __name__ == "__main__":
    main()
