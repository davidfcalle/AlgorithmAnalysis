def median_pos( pos ):
    if pos % 2 == 0:
        return (pos / 2 ) - 1
    else:
        return pos / 2

def median_helper( S , V):
    return median( S , V, 0 ,len( S ) , 0 , len( V )  )

def menor( a ,b ):
    if a < b :
        return a
    else:
        return b
def median( S , V , si , sf, vi, vf ):
    ms = ( sf - si ) / 2
    mv = ( vf - vi ) / 2
    if ( sf - si ) % 2 == 0:
        if sf - ms == 1:
            return menor( S[ ms + 1] , V[mv - 1] )
        if S[ ms ] < V[ mv ]:
            ms = ms + 1
            si = ms
            vf = mv
        else:
            mv = mv + 1
            vi = mv
            sf = ms
    else:
        #caso base
        if( sf == si ):
            return menor( S[ms] , V[mv] )

        if S[ ms ] < V[ mv ]:
            si = ms
            vf = mv
        else:
            vi = mv
            sf = ms
    return median( S , V , si , sf, vi, vf )


if __name__ == '__main__':
    S = [1,2,3,4]
    V = [2,5,6,100]
    print median_helper(S , V)
