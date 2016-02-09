def partition (S,L,R):
    pivot = S[ R ]
    i = L
    for j in range( L , R  ):
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
    if L < R:
        index = partition( S , L , R)
        quick_sort( S , L , index - 1)
        quick_sort( S, index + 1 , R )

def quick_sort_helper(S):
    quick_sort( S , 0 , len(S) - 1 )
