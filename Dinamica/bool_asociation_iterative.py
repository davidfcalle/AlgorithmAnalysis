# Basado en: http://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/

def parenthesization_iterative( symbols,  operators,  n, F, T ):

    #se llena la diagonal con valores, es decir, evaluarse asi mismo.
    for i in range( n ):
        F[i][i] = 0
        T[i][i] = 0
        if Symbols[i] == "T":
            T[i][i] = 1
        else:
            F[i][i] = 1

    for gap in range( 1, n ):
        i = 0;
        for j in range( gap, n ):
            T[i][j] = F[i][j] = 0
            for g in range( gap ):
                # Posicion del operando final en la prentizacion.
                k = i + g

                # Calculamos el total T( i, j )
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]

                if operators[ k ] == "and":
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += ( ( tik * tkj ) - T[i][k] * T[k+1][j] )
                elif operators[ k ] == "or":
                    F[i][j] += F[i][k] * F[k+1][j]
                    T[i][j] += ( ( tik * tkj ) - F[i][k] * F[k+1][j] )
                else:
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]

            i = i + 1

def print_matrix( M ):
    for row in M:
        print row

if __name__ == "__main__":
    Symbols = "TTFT"
    Operators= [ "or" , "and" , "xor" ]
    n = len( Symbols )
    T = [ None ] * n
    F = [ None ] * n
    for k in range( len( T ) ) :
        T[ k ] = [ None ] * n
        F[ k ] = [ None ] * n

    parenthesization_iterative( Symbols,  Operators,  n, F, T )

    print "Cantidad de parentizaciones posibles para que la expresion %s sea verdadera: %i" %( Symbols, T[0][n-1] )
    print_matrix( T );
    print "Cantidad de parentizaciones posibles para que la expresion %s sea false: %i" %( Symbols, F[0][n-1] )
