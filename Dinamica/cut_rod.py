def cut_rod_rec( prices , n ):
    if n == 0:
        return 0
    max_price = -999
    for k in range( n ):
        max_price = max( max_price , prices[ k ] + cut_rod_rec( prices , n - k - 1 ) )
    return max_price

def cut_rod_mem( prices , n  , memo ):
    if n == 0:
        return 0
    if memo[ n  - 1 ] is not None:
        return memo[ n - 1 ] 
    max_price = -999
    for k in range( n ):
        max_price = max( max_price , prices[ k ] + cut_rod_mem( prices , n - k - 1, memo ) )
    memo[ n - 1 ] = max_price 
    return max_price

def cut_rod_it( prices , n ):
    aux = [ None ] * ( n + 1 )
    aux[ 0 ] = prices[ 0 ]
    for i in range( 1 , n ): #desde el 1 hasta el valor de n
        # hay que calcular  el posible corte que se puede hacer para ese rango
        max_cut = prices[ i ]
        for k in range( 0 , i ):
            max_cut = max( max_cut , prices[ k ] + aux[ i - k - 1 ]  )
        aux[ i ] = max_cut
    return aux[ n - 1 ]

def cut_cod_it_conf( prices , n ):
    aux = [ None ] * ( n )
    cuts = [ None ] * ( n )
    aux[ 0 ] = prices[ 0 ]
    cuts[ 0 ] = 0
    for i in range( 1 , n ): #desde el 1 hasta el valor de n
        # hay que calcular  el posible corte que se puede hacer para ese rango
        max_cut = prices[ i ]
        cut = i
        for k in range( 0 , i ):
            new = max( max_cut , prices[ k ] + aux[ i - k - 1 ]  )
            if max_cut < new:
                max_cut = new 
                cut = k
        cuts[ i ] = cut
        aux[ i ] = max_cut  
    found = False
    index = n - 1
    ret = []
    while index > 0:
        # hay que ver en cuanto se hizo el corte
        cut_length = cuts[ index ]
        ret.append( cut_length + 1 )
        index = index - cut - 1 # menos 1 para que se mueva bien ya que el vector empieza en cero
    return ret






if __name__ == "__main__":
    prices = [  1 , 5 , 8 , 9 ]
    #print pricesx
    memo = [ None ] * len( prices )
    print cut_rod_rec( prices , len( prices ) )
    print cut_rod_mem( prices , len( prices ) , memo )
    print cut_rod_it( prices , len( prices ) )
    print cut_cod_it_conf( prices , len( prices ) )