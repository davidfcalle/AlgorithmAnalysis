from sets import Set

def count_repeated( list ):
    set = Set()
    for i in range( 0 , len( list ) ):
        for j in range ( i + 1 , len(list) ):
            if list[ i ] == list[ j ]:
                set.add( list[i] )
    return len( set )

def count_alternative( list ):
    s = Set()
    for item in list:
        s.add(item)
    return len( list ) - len( s )

if __name__ == '__main__':
    print count_repeated([1,2,2,3,2,1,2,3,4,6])
