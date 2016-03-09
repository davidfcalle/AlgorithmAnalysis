from fractions import gcd

def main():
    p = [ 2 , 10 , 25 ]
    print cut_square( p , len( p ) , len( p ) )


def split_rectangle( width , height , prices ):
    d_max = max( width , height )
    d_min = min( width , height )
    max_square_length = d_min
    if max_square_length == 0:
        return cut_square( prices , d_max , d_max  ) # si es un cuadrado pues que calcule el del cuadrado
    else:
        # lo debo partir en un cuadrado y que vuelva a recurrir
        h = d_min
        l = d_max - max_square_length
        if width == 1 or height == 1: #uno de los lados es uno, no hay nada que ver la mejor opcion es n cuadrados de tam 1
            return ( max( width , height ) * prices[ 0 ] )
        return cut_square( prices , max_square_length , max_square_length ) + split_rectangle( h , l , prices )

def cut_square( prices , width , height ):
    if width <= 0 or height <= 0:
        return 0
    else:
        q = -99999 # - infinito
        total = 0
        if height != width :
            return split_rectangle( width , height , prices )
        else:
            for i in range( width ):
                right = cut_square( prices , width - ( i + 1 ) , i + 1 )
                bottom_left = cut_square( prices , i + 1 ,  height - ( i + 1 ) )
                bottom_right = cut_square( prices , width - ( i + 1 ) ,  height - ( i + 1 ) )
                q = max( q , prices[ i ] + right + bottom_right + bottom_left )
            return q
if __name__ == '__main__':
    main()
