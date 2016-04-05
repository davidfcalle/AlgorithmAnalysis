


def get_sum( A , i , j ):
    sum = 0
    for k in range( i , j ):
        sum = sum + A[ k ]
    return sum

def max_sub_cont( A ):
    maximum = -999999
    i = 0
    j = 0
    while j >= i and j < len( A ) :
        max1 = get_sum( A, i, j )
        max2 = max1 + A[ j ]
        j = j + 1
        if max2 <= max1:
            i = j
            maximum = max1
        else:
            maximum = max2
    print "%i - %i" % ( i , j )
    print "max: %i" % ( maximum )



def main():
    A = [ 1 , 2  , 4 , -1 , 10  , 2 , -80 , 20 ]
    max_sub_cont( A )
if __name__ == '__main__':
    main()
