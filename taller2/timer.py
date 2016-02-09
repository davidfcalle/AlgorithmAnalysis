import time

def say_hello(name, last):
    print "Hi %s %s" % (name , last)

def count_time( function , *args ):
    t0 = time.clock( )
    function( *args )
    t1 = time.clock( )
    return t1 - t0

if __name__ == '__main__':
    time = count_time( say_hello , "david", "calle")
    print time
