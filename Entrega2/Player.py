from client import *
from copy import copy, deepcopy
import Queue as Q
import random

class Player(object):
    Taquin = [[]]

    def __init__( self , url="http://localhost:8080" , size = 2 , pid = 1 , name="DCD" , oid = 1):
        print "entra const"
        self.url = url
        self.size = int( size )
        self.Taquin = \
                  [ [ 0 for i in range( self.size ) ] \
                    for j in range( self.size ) ]
        self.pid = pid
        self.i = self.size - 1
        self.j = self.size - 1
        self.name = name
        self.oid = oid #id del oponente
        count = 1
        for i in range( self.size ):
            for j in range( self.size ):
                self.Taquin[ i ][ j ] = count
                count = count + 1
        #self.play() #quitar en produccion
        self.Taquin[ self.size - 1 ][ self.size - 1] = None
        


    def shuffle( self ):
        moves = []
        for k in range( self.size + 5 ):
            move = self.random_move(  )
            moves.append( move )
            self.move( move , False )   
        return moves
            
    def get_valid_moves( self ):
        valid_moves = []
        if self.i > 0:
            valid_moves.append( 2 )
        if self.i < self.size - 1:
            valid_moves.append( 3 )
        if self.j > 0:
            valid_moves.append( 1 )
        if self.j < self.size - 1:
            valid_moves.append( 0 )
        return valid_moves

    def random_move( self ):
        moves = self.get_valid_moves()
        print moves
        return moves[ random.randint( 0 , len( moves ) - 1 ) ]

    def play( self ):
        raw_input("Press Enter to continue...")
        generateBoard( self.url , self.Taquin , self.size - 1 , self.size - 1 )
        raw_input("Press Enter to continue...")
        create_player( self.url , self.pid , self.name )
        raw_input("Press Enter to continue...")
        challenge( self.url , self.Taquin , self.size - 1 , self.size - 1 , self.oid )

    def swap( self , initial_i , initial_j , end_i , end_j ):
        copy = self.Taquin[ initial_i ][ initial_j ]
        self.Taquin[ initial_i ][ initial_j ] = self.Taquin[ end_i ][ end_j ]
        self.Taquin[ end_i ][ end_j ] = copy

    def move( self , direction , isCopy ):
        if direction == 0:
            
            if not isCopy:
                print "        Movimiento derecha %i %i" % ( self.i , self.j )
                move_right( self.url , self.pid )
            self.swap( self.i , self.j , self.i , self.j + 1 )
            self.j = self.j + 1
        elif direction == 1:
             if not isCopy:
                print "        Movimiento izquierda %i %i" % ( self.i , self.j )
                move_left( self.url , self.pid )
             self.swap( self.i , self.j , self.i , self.j - 1 )
             self.j = self.j - 1
        elif direction == 2:
            if not isCopy:
                print "         Movimiento arriba %i %i" % ( self.i , self.j )
                move_up( self.url , self.pid )
            self.swap( self.i , self.j , self.i - 1 , self.j )
            self.i = self.i - 1
        elif direction == 3:
            if not isCopy:
                print "         Movimiento abajo %i %i" % ( self.i , self.j )
                move_down( self.url , self.pid )
            self.swap( self.i , self.j , self.i + 1 , self.j )
            self.i = self.i + 1
        else:
            print "Invalid Move!"
        if not isCopy:
            self.print_taquin()

    def is_ordered( self ):
        array = []
        count = 0
        for i in range( len( self.Taquin ) ):
            for j in range( len( self.Taquin ) ):
                array.append( self.Taquin[ i ][ j ] )
        current = deepcopy( array )
        array.sort()
        array.append( None ) # pongo uno extra para que el None quede al final
        array.pop( 0 )
        for k in range( len( array ) ):
            if array[ k ] != current[ k ]:
                return False
        return True

    def print_taquin( self ):
        print "********************************************\n"
        s = [[str(e) for e in row] for row in self.Taquin]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)
        print "********************************************\n"

    def simulate_player( self ): 
        print "*************** Jugador *************************"
        while not self.is_ordered():
            queue = Q.PriorityQueue()
            moves = self.get_valid_moves()
            print "Hay %i movimientos" % ( len( moves ) )
            for movement in moves:
                player_copy = deepcopy( self )
                player_copy.move( movement , True )
                queue.put( Movement( player_copy.Taquin , player_copy.i , player_copy.j , movement ) )
            best = queue.get()
            raw_input("Press Enter to continue...")
            self.move( best.movement , False )
            print "El mejor movimiento es: %i %i " % ( best.i , best.j )
        #obtener todos los posibles movimientos el movimiento actual



class Movement:

    def __init__( self, Taquin , i , j , movement ):
        self.Taquin = deepcopy( Taquin )
        self.correctly_placed = self.count_correctly_placed()
        self.exact_total_distance = self.count_exact_total_distance()
        print " Se crea un movimiento con puestos %i y distancia %i " % ( self.correctly_placed , self.exact_total_distance )
        self.i = deepcopy( i )
        self.j = deepcopy( j )
        self.movement = deepcopy( movement )

 
    def count_exact_total_distance( self ):
        count = 0
        array = []
        total_distance = 0
        for i in range( len( self.Taquin ) ):
            for j in range( len( self.Taquin ) ):
                count = count + 1
                value = self.Taquin[ i ][ j ]
                if value is not None:
                    total_distance = total_distance + abs( value - count )
        return total_distance

    def count_correctly_placed( self ):
        array = []
        count = 0
        for i in range( len( self.Taquin ) ):
            for j in range( len( self.Taquin ) ):
                array.append( self.Taquin[ i ][ j ] )
        current = deepcopy( array )
        array.sort()
        array.append( None ) # pongo uno extra para empezar desde 1
        array.pop( 0 )
        for k in range( len( array ) ):
            if array[ k ] != current[ k ]:
                count = count + 1
        return count

    def __cmp__( self , other ):
        first = cmp( self.correctly_placed , other.correctly_placed )
        if first != 0:
            return first
        return cmp( self.exact_total_distance , other.exact_total_distance )




 
    


