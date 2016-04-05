"""
    Ejercicio de parentizacion , es es la matriz de verdaderos, f es el amatriz de falsos
"""
def total( Symbols , Operators,  i , j , T , F ):
    return true( Symbols , Operators , i , j , T , F ) + false( Symbols , Operators , i , j , T , F )

def false( Symbols , Operators , i , j , T , F ):
    if i == j and Symbols[ i ] == "T":
        return 0
    elif i == j and Symbols[ i ] == "F":
        return 1
    else:
      #verificar si ya ha sido calculado
      if F[ i ][ j ] is not None:
          return F[ i ][ j ]
      count = 0
      for k in range( i , j ):
          # hay que coger cada operador para evaluar
          if Operators[ k ] == "and" :
             a = total( Symbols , Operators , i , k , T , F ) * total( Symbols , Operators , k + 1 , j , T , F )
             b = true( Symbols , Operators , i , k , T , F   ) * true( Symbols , Operators , k + 1  , j  , T , F )
             count = count + ( a - b ) 
          elif Operators[ k ] == "or" :
              a = false( Symbols , Operators , i , k , T , F   )
              b = false( Symbols , Operators , k + 1  , j  , T , F )
              count = count + ( a * b )
          else:
             # es un XOR
             a = true( Symbols , Operators , i , k , T , F ) * true( Symbols , Operators , k + 1 , j , T , F )
             b = false( Symbols , Operators , i , k , T , F ) * false( Symbols , Operators , k + 1 , j , T , F ) 
             count = count + ( a + b )
      F[ i ][ j ] = count
      return count

def true(  Symbols , Operators , i , j , T , F ): 
    if i == j and Symbols[ i ] == "T":
        return 1
    elif i == j and Symbols[ i ] == "F":
        return 0
    else:
      if T[ i ][ j ] is not None:
         return T[ i ][ j ]
      count = 0
      for k in range( i , j ):
          # hay que coger cada operador para evaluar)
          if Operators[ k ] == "and" :
              a = true( Symbols , Operators , i , k , T , F   )
              b = true( Symbols , Operators , k + 1  , j  , T , F )
              count = count + ( a * b )
          elif Operators[ k ] == "or" :
             a = total( Symbols , Operators , i , k , T , F ) * total( Symbols , Operators , k + 1 , j , T , F )
             b = false( Symbols , Operators , i , k , T , F ) * false( Symbols , Operators , k + 1  , j  , T , F )
             count = count + ( a - b )  
          else:
             a = true( Symbols , Operators , i , k , T , F ) * false( Symbols , Operators , k + 1 , j , T , F )
             b = false( Symbols , Operators , i , k , T , F ) * true( Symbols , Operators , k + 1 , j , T , F ) 
             count = count + ( a + b )
      T[ i ][ j ] = count
      return count

def parenthesization_true( Symbols, Operators ):
    T = [ None ] * len( Symbols )
    F = [ None ] * len( Symbols )
    for k in range( len( T ) ) :
        T[ k ] = [ None ] * len( Symbols )
        F[ k ] = [ None ] * len( Symbols )
    # se llena la diagonal de los valores
    for d in range( len( T ) ):
        if Symbols[ d ] == "T":
            T[ d ][ d ] = 1
            F[ d ][ d ] = 0
        else:
            T[ d ][ d ] = 0
            F[ d ][ d ] = 1
    result =  true( Symbols , Operators , 0 , len( Symbols ) - 1 , T , F )
    print_matrix( T )
    return result

def print_matrix( M ):
    for row in M:
        print row
            

if __name__ == "__main__":
    Symbols = "TTFT"
    Operators= [ "or" , "and" , "xor" ]
    print "Resultado %s es %i" % ( Symbols ,  parenthesization_true( Symbols , Operators ) )

