

def knapsack_recurisive( values , weights , w  , i ):
    print i
    if i < 0 :
        return 0
    else :
        # verifico si quepo
        if w - weights[ i ] < 0:
            return knapsack_recurisive( values , weights , w , i - 1 )
        else:
             # si quepo y necesito el maximo
            maxi = max( knapsack_recurisive( values , weights , w , i - 1 ) , knapsack_recurisive( values , weights , w - weights[ i ] , i - 1 ) + values[ i ] )
            return maxi


def knapsack_iterative( values , weights , w ):
    M= [ None ] * ( w + 1 )
    W= [ None ] * ( w + 1 )
    M[ 0 ] = -999999999
    W[ 0 ] = -999999999  

    for i in range( 1, w + 1 ):
        maxi = M[ i - 1 ]
        maxiw = W[ i - 1 ]
        i_max = -1
        for j in range( len( weights ) ):    
            if weights[j] <= i:
                if  i - weights[ j ] > 0:
                    print "QWERTYUIOKO"
                    sum = values[j] + M[ i - weights[j] ]
                    sumw = weights[j] + W[ i - weights[j] ]
                else:
                    print "WWW i = %i cabe j = %i ,axi = %i" % (i, j, maxi )
                    sum  = values[ j ]
                    sumw = weights[ j ]
                if sum > maxi:
                    maxi = int( sum )
                    maxiw = sumw
                    i_max = j
                    print maxi
                    print i_max
        if i_max >= 0:
            M[i] = maxi
            W[i] = maxiw
            weights.pop( i_max )
            values.pop( i_max )
        else:
            if i - W[ i - 1 ]  > 0:
                M[ i ] = M[ i - 1 ] + M[ i - W[ i - 1 ] ]
                W[ i ] = W[ i - 1 ] + W[ i - W[ i - 1 ] ]
            else:
                M[ i ] = M[ i - 1 ]
                W[ i ] = W[ i - 1 ]
                
    return M


if __name__ == "__main__":
    weights = [3, 5, 7, 1, 9]
    values = [8, 1, 1, 7, 5]
    w = 12
    print "res %i" % knapsack_recurisive( values, weights, w, len( weights ) - 1 )
    print knapsack_iterative( values , weights , w )