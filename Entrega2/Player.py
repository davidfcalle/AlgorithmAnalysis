from client import *
from copy import copy, deepcopy
import Queue as Q
import random

class Player(object):
    Taquin = [[]]

    def __init__( self , url="http://localhost:8080" , size = 2 , pid = 1 , name="DCD" , oid = 1):
        self.url = url
        self.size = int( size )
        self.Taquin = \
                  [ [ 0 for i in range( self.size ) ] \
                    for j in range( self.size ) ]
        self.pid = pid
        self.name = name
        self.oid = oid #id del oponente
    """
        constructor para jugar solo 
    """
    def __init__( self , url="http://localhost:8080" , size = 2 , pid = 1 , name="DCD" , oid = 1 , Taquin  = [[]] , i = 0 , j = 0):
        self.url = url
        self.size = int( size )
        self.Taquin = \
                  [ [ 0 for i in range( self.size ) ] \
                    for j in range( self.size ) ]
        self.pid = pid
        self.name = name
        self.oid = oid #id del oponente
        self.Taquin = Taquin
        self.i = i 
        self.j = j
        self.Taquin[ i ][ j ] = None


    def get_challenge( self ):
        challenge = get_board( self.url , self.pid )
        self.size = len( challenge["currentState"] ) 
        print "el tam del reto es de %i" % self.size
        self.Taquin = \
                  [ [ 0 for i in range( self.size ) ] \
                    for j in range( self.size ) ]
        for i in range( len( challenge["currentState"] ) ):
             for j in range( len( challenge["currentState"] ) ):
                            try:
                                self.Taquin[ i ][ j ] = int( challenge["currentState"][ i ][ j ] )
                            except:
                                print "error al parsear %s" % challenge["currentState"][ i ][ j ]
                                self.Taquin[ i ][ j ]  = None
        self.i = int( challenge["blank"]["row"] )
        self.j = int( challenge["blank"]["column"] )
        self.Taquin[ self.i ][ self.j ] = None
        self.print_taquin()

    def compete( self ):
        raw_input( " Oprime enter una vez te hallan retado" ) 
        self.get_challenge( )
        self.simulate_player( )
        
    def initialize_ordered_matrix( self ):
        count = 1
        for i in range( self.size ):
            for j in range( self.size ):
                self.Taquin[ i ][ j ] = count
                count = count + 1
        self.Taquin[ self.size - 1 ][ self.size - 1] = None
        self.i = self.size - 1
        self.j = self.size - 1

     
    def add_challenge( self , Matrix , i , j  ):
        challenge( self.url , Matrix , i , j , self.oid )

    def shuffle( self ):
        moves = []
        for k in range( self.size + 5 ):
            move = self.random_move(  )
            moves.append( move )
            #raw_input("Press Enter to continue...")
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
        return moves[ random.randint( 0 , len( moves ) - 1 ) ]

    def register( self ):
        create_player( self.url , self.pid , self.name )

    def challenge( self ):
        """ por ahora el challenge es retar con lo que tambien me pusieron """
        challenge( self.url , self.Taquin , self.i , self.j , self.oid )

    def create_player( self ):
        generateBoard( self.url , self.Taquin , self.i , self.j )
        self.register( )

    def swap( self , initial_i , initial_j , end_i , end_j ):
        copy = self.Taquin[ initial_i ][ initial_j ]
        self.Taquin[ initial_i ][ initial_j ] = self.Taquin[ end_i ][ end_j ]
        self.Taquin[ end_i ][ end_j ] = copy

    """
        funcion que mueve al jugador en la direccion direction, el segundo paramtero isCopy es para que las copias de jugadores no alteren el estado del servidor
        si isCopy es True, no envia nada al servidor
    """
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
             "Invalid Move!"
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
        print "********************************************"
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
            #raw_input("Press Enter to continue...")
            self.move( best.movement , False )
            #print "El mejor movimiento es hacia %i %i " % ( best.i , best.j )
        #obtener todos los posibles movimientos el movimiento actual



class Movement:

    def __init__( self, Taquin , i , j , movement ):
        self.Taquin = deepcopy( Taquin )
        self.correctly_placed = self.count_correctly_placed()
        self.exact_total_distance = self.count_exact_total_distance()
        #print " Se crea un movimiento con puestos %i y distancia %i " % ( self.correctly_placed , self.exact_total_distance )
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




 
    


