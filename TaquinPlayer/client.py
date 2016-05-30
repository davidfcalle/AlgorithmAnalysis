from random import randint
import json
import requests

"""
esta funcion genera una mtriz de nXn con numeros aleatorios
"""
def generate_matrix( n ):
    matrix = [ None ] * n
    for i in range( n ):
        matrix[i] = [ None ] * n

    for i in range( n ):
        for j in range( n ):
            matrix[i][j] = randint( 1, n )
    return matrix

"""
esta funcion recibe la matriz y la posicion x , y donde esta la posicion en blanco
"""
def generateBoard( domain , matrix , row , column ):
    body = {
        "currentState" : matrix,
        "movements" : 0,
        "blank" : { "row" : row , "column" : column }
    }
    response = requests.post( domain + "/api/board/new/",  data = json.dumps( body ), headers={ "content-type" : "application/json" } )

"""
esta funcion recibe la matriz y la posicion x , y donde esta la posicion en blanco
"""
def challenge( domain , matrix , row , column, opponentId ):
    body = {
        "currentState" : matrix,
        "movements" : 0,
        "blank" : { "row" : row , "column" : column }
    }
    #print domain + "/api/player/%i/challenge/" % ( opponentId )
    response = requests.post( domain + "/api/player/%i/challenge" % ( opponentId ) ,  data=json.dumps(body), headers={"content-type": "application/json"})

"""
    funcion que retorna la matriz del reto que hizo un jugador
"""
def get_challenge( domain , pId ):
    r = requests.get( domain + "/api/board/%i/" % ( pId ) )

"""
    funcion que retorna la matriz del reto que hizo un jugador
"""
def get_board( domain, pId ):
    r = requests.get( domain + "/api/board/%i/" % ( pId ))
    return json.loads( r.text )

"""
esta funcion recibe  el pid del jugador actual y mueve la ficha en blanco a la izquerda
"""
def move_left( domain , pId ):
    response = requests.post( domain + "/api/player/%i/board/move/left/" % ( pId ) )

"""
esta funcion recibe  el pid del jugador actual y mueve la ficha en blanco a la derecha
"""
def move_right( domain , pId ):
    response = requests.post( domain + "/api/player/%i/board/move/right/" % ( pId ) )

"""
esta funcion recibe  el pid del jugador actual y mueve la ficha en blanco a la arriba
"""
def move_up( domain , pId ):
    response = requests.post( domain + "/api/player/%i/board/move/up/" % ( pId ) )

"""
esta funcion recibe  el pid del jugador actual y mueve la ficha en blanco hacia abajo
"""
def move_down( domain , pId ):
    response = requests.post( domain + "/api/player/%i/board/move/down/" % ( pId ) )

def create_player(  domain , pId  , name ):
    response = requests.post( domain + "/api/player/%i/new/%s/" % ( pId , name ) )


def check( domain , pid):
    move_right( domain , pid )
    move_right( domain , pid )
    move_right( domain , pid )
    move_right( domain , pid )
    move_right( domain , pid )
    move_right( domain , pid )

    move_left( domain , pid )
    move_left( domain , pid )
    move_left( domain , pid )
    move_left( domain , pid )
    move_left( domain , pid )
    move_left( domain , pid )

    move_down( domain , pid )
    move_down( domain , pid )
    move_down( domain , pid )
    move_down( domain , pid )
    move_down( domain , pid )
    move_down( domain , pid )

    move_up( domain , pid )
    move_up( domain , pid )
    move_up( domain , pid )
    move_up( domain , pid )
    move_up( domain , pid )
    move_up( domain , pid )