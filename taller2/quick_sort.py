def partition (S,L,R):
    pivot = S[ R ]
    i = L
#    print " L-R %i-%i" % (L, R)
    for j in range( L , R  ):
#        print "j %i" % j
        if S[ j ] <= pivot:
            tmp = S[ i ]
            S[ i ] = S[ j ]
            S[ j ] = tmp
            i = i + 1
    tmp = S[ i ]
    S[ i ] = S[ R ]
    S[ R ] = tmp
    return i



def quick_sort(S,L,R):
    print S
    if L < R:
        index = partition( S , L , R)
        print "Index %i"  % index
        quick_sort( S , L , index - 1)
        quick_sort( S, index + 1 , R )
