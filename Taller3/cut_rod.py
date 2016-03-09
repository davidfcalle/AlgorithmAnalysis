def cut_rod( p , n ):
    if n == 0:
        return 0
    q = -999
    for i in range( n ):
        #print "i: %i n: %i" % ( i - 1 , n - i )
        q = max( q , p[ i ] + cut_rod(  p , n - i - 1 ) )
    return q

def memoized_cut_rod( p , n ):
    r = [ -9999 ] * 10
    return memoized_cut_rod_aux( p , n , r )

def memoized_cut_rod_aux( p , n , r ):
    if r[ n ] >= 0:
        return r[ n ]
    if n == 0:
        q = 0
    else:
        q = -9999
        for i in range( n ):
            q = max( q , p[ i ] + memoized_cut_rod_aux(  p , n - i - 1 , r) )
    r[ n ] = q
    return q

def main():
    p = [ 2 , 4 , 7 , 6]
    print cut_rod( p , len( p ) )
    print memoized_cut_rod( p , len( p ) )

if __name__ == '__main__':
    main()
