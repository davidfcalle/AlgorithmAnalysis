def fibo_rec( n ):
    if n <= 1 :
        return n
    else:
        return fibo_rec( n - 1 ) + fibo_rec( n - 2 )

def fib_memo( n , arr ):
    if arr[ n ] is not None:
        return arr[ n ]
    else:
        if n <= 1:
            arr[ n ] = n
            return arr[ n ]
        else:
            arr[ n ] = fib_memo( n - 1 , arr ) + fib_memo( n - 2 , arr )
            return arr[ n ]

def fib_iterativo( n ):
    arr = [ None ] * ( n + 1 )
    arr[ 0 ] = 0
    arr[ 1 ] = 1
    for i in range( 2 ,  n + 1 ):
        arr[ i ] = arr[ i - 1 ] + arr[ i - 2 ]
    return arr[ n ]



if __name__ == "__main__" :
    print fibo_rec( 700 )
    print "fin rec"
    print fib_memo( 700 , [ None ] * 7000  )
    print "fin memo"
    print fib_iterativo( 700 )
    print "fin iterativo"