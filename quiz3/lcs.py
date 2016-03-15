

def lcs_recursive( S1, i1 , S2 , i2 ):
        if i1 < 0 or i2 < 0:
            return 0
        elif  S1[ i1 ] == S2[ i2 ]:
            return 1 + lcs_recursive( S1 , i1 -1 , S2, i2 -1 )
        else:
            return max( lcs_recursive( S1 , i1 -1 , S2 , i2 ) , lcs_recursive( S1 , i1  , S2 , i2 - 1 )  )

def lcs_memoized_helper( S1 , S2 ):
    matrix = [ None ] * len( S1 )
    for l in range( len( S1 )  ):
        matrix[ l ] = [ None ] * len( S2 )
    print lcs_memoized( S1 , len(S1) -1 , S2 , len( S2 ) -1 , matrix)
    print matrix

def lcs_memoized( S1 , i1 , S2 , i2 , matrix ):
    if i1 < 0 or i2 < 0:
        return 0
    elif  S1[ i1 ] == S2[ i2 ]:
        if matrix[ i1 ][ i2 ] > 0 :
            return matrix[ i1 ][ i2 ]
        matrix[ i1 ][ i2 ] = 1 + lcs_memoized( S1 , i1 -1 , S2, i2 -1 , matrix )
        return matrix[ i1 ][ i2 ]
    else:
        matrix[ i1 ][ i2 ] = max( lcs_memoized( S1 , i1 -1 , S2 , i2, matrix ) , lcs_memoized( S1 , i1  , S2 , i2 - 1  , matrix ) )
        return matrix[ i1 ][ i2 ]

def lcs_memoized_iterative(  S1 , S2 ):
    """inicialiczacion de matriz"""
    matrix = [ 0 ] * len( S1 )
    for l in range( len( S1 )  ):
        matrix[ l ] = [ 0 ] * len( S2 )
    """ metodo """
    i1 = len( S1 )
    i2 = len( S2 )
    max_l = 0
    for i in range( i1 ):
        for j in range( i2 ):
            if S1[ i ] == S2[ j ]:
                if i == 0 or j == 0:
                    matrix[ i ][ j ] = 1
                else:
                    matrix[ i ][ j ] = 1 + matrix[ i - 1 ][ j - 1 ]
            else:
                if i == 0 or j == 0:
                    matrix[ i ][ j ] = 0
                else:
                    matrix[ i ][ j ] = max( matrix[ i ][ j - 1 ] , matrix[ i - 1 ][ j ] )
    """ obtencion de configuracion """
    result = []
    finished = False
    i = len( S1 ) - 1
    j = len( S2 ) - 1
    while finished == False :
        if i == 0 or j == 0:
            if S1[ i ] == S2[ j ]:
                result.insert( 0 , S1[ i ] )
                finished = True
            else:
                if i == j:
                    finished = True
                else:
                    if i > j:
                        i = i - 1
                    else:
                        j = j - 1
        else:
            if S1[ i ] == S2[ j ]:
                result.insert( 0 , S1[ i ] )
                i = i - 1
                j = j - 1
            else:
                if matrix[ i - 1 ][ j ] < matrix[ i ][ j - 1 ]:
                    j = j - 1
                else:
                    i = i -1
    return result


def main():
    #S1 =    [ "A", "B", "C", "B", "D", "A", "B" ]
    #S2 = [ "B", "D", "C", "A", "B", "A" ]
    #S1 =    [ "A", "B"]
    S1 = [ 1, 0, 0, 1, 0, 1, 0, 1 ]
    #S2 = [ "B", "A" ]
    S2 = [ 0, 1, 0, 1, 1, 0, 1, 1, 0 ]
    #print lcs_recursive(  S1 , len(S1) -1 , S2 , len( S2 ) - 1 )
    print lcs_memoized_iterative( S1 , S2 )

if __name__ == '__main__':
    main()
