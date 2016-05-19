from Corte import *


if __name__ == "__main__":
    corte1 = Corte( 1 , 1 , 2 )
    corte2 = Corte( 5 , 2 , 2 )
    corte3 = Corte( 2 , 1 , 2 )
    cortes = []
    cortes.append( corte1 )
    cortes.append( corte2 )
    cortes.append( corte3 )
    tela = Tela( 6 , 2 , cortes )
    res =  tela.cortar()
    print([str(item) for item in res])
    raw_input("Fin!")

