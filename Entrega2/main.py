import client as taquin
from Player import Player

def main():
    print "Entra"
    player =  Player()
    print "Entra"
    player.print_taquin()
    print "Entra"
    player.shuffle()
    print "Entra"
    player.simulate_player()
    print "Entra"

    #player2 =  Player(oid=2,name="Silva",pid=2)
    #player2.shuffle()


        
if __name__ == '__main__':
    main()