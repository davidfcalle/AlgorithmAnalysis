"""
    Ejercicio de parentizacion
"""
def total( Symbols , Operators,  i , j ):
    return true( Symbols , Operators , i , j ) + false( Symbols , Operators , i , j )

def false( Symbols , Operators , i , j ):
    if i == j and Symbols[ i ] == "T":
        return 0
    elif i == j and Symbols[ i ] == "F":
        return 1
    else:
      count = 0
      for k in range( i , j ):
          # hay que coger cada operador para evaluar
          if Operators[ k ] == "and" :
             a = total( Symbols , Operators , i , k ) * total( Symbols , Operators , k + 1 , j )
             b = true( Symbols , Operators , i , k   ) * true( Symbols , Operators , k + 1  , j  )
             count = count + ( a - b ) 
          elif Operators[ k ] == "or" :
              a = false( Symbols , Operators , i , k   )
              b = false( Symbols , Operators , k + 1  , j  )
              count = count + ( a * b )
          else:
             a = true( Symbols , Operators , i , k ) * true( Symbols , Operators , k + 1 , j )
             b = false( Symbols , Operators , i , k ) * false( Symbols , Operators , k + 1 , j ) 
             count = count + ( a + b )
      return count

def true(  Symbols , Operators , i , j ): 
    if i == j and Symbols[ i ] == "T":
        return 1
    elif i == j and Symbols[ i ] == "F":
        return 0
    else:
      count = 0
      for k in range( i , j ):
          # hay que coger cada operador para evaluar)
          if Operators[ k ] == "and" :
              a = true( Symbols , Operators , i , k   )
              b = true( Symbols , Operators , k + 1  , j  )
              count = count + ( a * b )
          elif Operators[ k ] == "or" :
             a = total( Symbols , Operators , i , k ) * total( Symbols , Operators , k + 1 , j )
             b = false( Symbols , Operators , i , k   ) * false( Symbols , Operators , k + 1  , j  )
             count = count + ( a - b )  
          else:
             a = true( Symbols , Operators , i , k ) * false( Symbols , Operators , k + 1 , j )
             b = false( Symbols , Operators , i , k ) * true( Symbols , Operators , k + 1 , j ) 
             count = count + ( a + b )
      return count

def parenthesization_true( Symbols, Operators ):
    return true( Symbols , Operators , 0 , len( Symbols ) - 1 )

if __name__ == "__main__":
    Symbols = "TTFT"
    Operators= [ "or" , "and" , "xor" ]
    print parenthesization_true( Symbols , Operators )

