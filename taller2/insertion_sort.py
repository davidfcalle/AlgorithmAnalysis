def insertion_sort(S):
    for j in range ( 1 , len(S) ):
        k = S[j]
        i = j - 1
        while( i > 0 and S[i] > k):
            S[ i + 1 ] = S[ i ]
            i = i - 1
        S[ i + 1 ] = k
    return S
