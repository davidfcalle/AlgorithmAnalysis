def esPal( S , i , j ):
    esIgual = True
    while esIgual == True and i <= j:
        if S[ i ] != S[ j ] :
            print S[i:j] 
            esIgual = False
        i = i + 1
        j = j - 1
    return esIgual

def pal( S , i , j ):
    if i > j:
        return 0
    elif esPal( S , i , j ) == True:
        return  j - i + 1
    else:
        return max( pal( S , i + 1 , j ) , pal( S ,  i , j - 1 ) )

def iterativo( S ):
    i = 0
    j = len( S ) - 1

   
if __name__ == "__main__":
    S = "seresaj"
    i = 0
    j = len( S ) - 1
    print pal( S , i , j )