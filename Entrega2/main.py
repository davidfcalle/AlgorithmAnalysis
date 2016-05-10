import client as taquin
from Player import Player

def main():
    player =  Player()
    player.play()
    player.print_taquin()
    player.shuffle()
    print "Fin del Shuffle"
    player.simulate_player()


    player2 =  Player( name="Silva" , pid=2 , oid=2 )
    player2.play()
    player2.print_taquin()
    player2.shuffle()
    player2.simulate_player()


        
if __name__ == '__main__':
    main()