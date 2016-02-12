import time

def count_time( function , *args ):
    t0 = time.clock( )
    function( *args )
    t1 = time.clock( )
    return t1 - t0
