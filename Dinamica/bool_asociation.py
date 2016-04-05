

def count_true( A , i , j , k ):
    if i == j and A[ i ] == True:
        return 1
    elif  i == j and A[ i ] == False:
        return 0
    else:
        # Toca evaluar  los operadores
        if  A[ k ] == "and" :
            
            
 
    

if __name__ == "__main__":
    print "Hello World!"
    expression = [ True , "and" , False , "or" ,  True ]