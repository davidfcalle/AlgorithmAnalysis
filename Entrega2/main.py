import client as taquin
from Player import Player

def main():
    player =  Player()
    player.print_taquin()
    player.shuffle()
    player.simulate_player()


    player2 =  Player( name="Silva" , pid=8 , oid=8 )
    player2.print_taquin()
    player2.shuffle()
    player2.simulate_player()


        
if __name__ == '__main__':
    main()