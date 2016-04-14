import math

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

def character_to_number( character ):
    for i in range( len( characters ) ):
        if characters[ i ] == character:
            return i
    return -1

def number_to_character( number  ):
    return characters[ number ]

def congruent( p , q ):
    return 3 % 4 == p % 4 and 3 % 4 == q % 4

def make_array( n ):
    M = []
    for i in range( len( n ) ):
        M.append( i )
    return M


def solve_brute_force( p , q ):
    for i in range( 0 , 10 ):
        for j in range( 0 , 10):
            if solve_ecuation( p , q , i , j ):
                return { "a" : i , "b" : j }

def solve_ecuation( p , q , a , b ):
    return  ( ( (a * p)  % q ) == 1 ) and ( (b * q)  % p == 1 )
"""
    La funcion asume que p y q son enteros primos
"""
def cipher_rabin( text , p , q ):
    M = make_array( text )
    cyphered_text = []
    if congruent( p , q ):
        n = p * q
        for i in range( len( M ) ):
            c = cipher( character_to_number( text[ i ] ) , n )
            cyphered_text.append( c )
        return cyphered_text
    else:
        raise Exception('No cumple con la congruencia') 
    return text
"""
    Funcion qeu cifra una letra
"""
def cipher( character , n ):
    return ( character * character )  % n 

"""
    funcion que se encarga de descifrar
    hay que resolver la ecuacion
    x2 === C mod N , donde n es la llave publica
"""
def decipher( text , p , q ):
    # se van a halar las 4 posibles raices que tiene
    solution = solve_brute_force( p , q )
    a = solution[ "a" ]
    b = solution[ "b" ]
    n = p * q
    for c in text:
        r1 = math.pow( c , ( p + 1 ) / 4 ) % p
        r2 =  ( -1 * ( math.pow( c , ( p + 1 ) / 4 )) % p )
        r3 = math.pow( c , ( q + 1 ) / 4 ) % q
        r4 =  (  -1 * ( math.pow( c , ( q + 1 ) / 4 ) )% q )
        #solucion 1
        s1 = int( ( r1 * q * b + r3 * p * a ) % n )
        s2 = int ( ( r1 * q * b + r4 * p * a ) % n )
        s3 = int ( ( r2 * q * b + r3 * p * a ) % n )
        s4 = int ( ( r2 * q * b + r4 * p * a ) % n )
        return ( s1 , s2 , s3 , s4 ,)

if __name__ == "__main__":
    text = cipher_rabin( "k"  , 7 , 11 )
    print text
    print decipher( text , 7 , 11 )
    