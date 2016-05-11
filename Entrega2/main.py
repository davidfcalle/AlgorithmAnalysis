import client as taquin
from Player import Player
"""
    metodo que carga un jugador con la configuracion
"""
def load_configuration( filename ):
    fp = open( filename )
    url = fp.readline()
    url = url.strip()
    pid = int( fp.readline() )
    oid = int( fp.readline() )
    name = fp.readline()
    challenge_size = int( fp.readline() )
    challenge_i_j = fp.readline()
    arg_list = challenge_i_j.split()
    i = arg_list[ 0 ]
    j = arg_list[ 1 ]
    matrix = []
    row = "whatever"
    while challenge_size > 0:
        if not row:
            break
        row = fp.readline()
        row = row.strip()
        row = row.split()
        row = map( int , row )
        if len( row ) == 0:
            break
        matrix.append( row )
    player = Player( url=url , size = challenge_size , pid = pid , oid = oid, i = i , j = j , Taquin = matrix)
    return player
        
   
def main():
    raw_input( "  ¿Listo? " )
    player = load_configuration( "C:\Users\david\Documents\Javeriana\Algoritmos\Entrega2\conf.txt" )
    player.create_player( )
    player.challenge( )
    raw_input( "  Listo para jugar  " )
    player.compete( )

    """
    player =  Player( name="DSD" , pid=1 , oid=2 , url="https://spark-davidcalle94301.c9users.io" , size = 2)
    player.initialize_ordered_matrix( )
    player.create_player( )
    player.shuffle( )
    raw_input( "  Fin jugador 1  " )

    
    player2  = Player( name="Bermeo"  , pid = 2 , oid = 1 , url = "https://spark-davidcalle94301.c9users.io" , size = 2 )
    player2.initialize_ordered_matrix( )
    player2.create_player( )
    player2.shuffle( )
    raw_input( "  Fin jugador 2  " )

    player.challenge( )
    player2.challenge( )
    
    
    player2.compete( )
    player.compete( )
    """

        
if __name__ == '__main__':
    main()