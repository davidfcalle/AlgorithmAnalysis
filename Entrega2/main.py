import client as taquin
from Player import Player

def main():

    player =  Player( name="David Calle" , pid=1 , oid=2 , url="http://localhost:8080" , size = 2)
    player.initialize_ordered_matrix( )
    player.create_player( )
    player.shuffle( )
    raw_input( "  Fin jugador 1  " )


    player2  = Player( name="Bermeo"  , pid = 2 , oid = 1 , url = "http://localhost:8080" , size = 2 )
    player2.initialize_ordered_matrix( )
    player2.create_player( )
    player2.shuffle( )
    raw_input( "  Fin jugador 2  " )

    player.challenge( )
    player2.challenge( )
    


    player.compete( )
    player2.compete( )

        
if __name__ == '__main__':
    main()