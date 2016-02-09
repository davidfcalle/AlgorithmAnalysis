import sys

def merge_sort( S , f , l ):
    if f < l :
        h = ( f + l ) / 2
        merge_sort( S , f , h )
        merge_sort( S , h + 1 , l )
        merge( S , f , h , l )

def merge( S , q , p , r ):
    i = 0
    j = 0
    f = S[ q : p + 1]
    l = S[ p + 1 : r + 1]
    f.append(sys.maxint)
    l.append(sys.maxint)
    for k in range( q , r + 1 ):
        if f[ i ] < l[ j ]:
            S[ k ] = f[ i ]
            i = i + 1
        else:
            S[ k ] = l[ j ]
            j = j + 1

def merge_sort_helper( S ):
    merge_sort( S , 0 , len(S) - 1 )
