# Basado en: http://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/ 
import itertools
def parenthesization_iterative( symbols,  operators,  n, F, T ,TT):

    #se llena la diagonal con valores, es decir, evaluarse asi mismo.
    for i in range( n ):
        F[i][i] = 0
        T[i][i] = 0
        if Symbols[i] == "T":
            T[i][i] = 1
            TT[ i ][ i ][ 0 ] = 1
        else:
            F[i][i] = 1
        
    for gap in range( 1, n ):
        i = 0;
        for j in range( gap, n ):
            T[i][j] = F[i][j] = 0
            for g in range( gap ):
                k = i + g
                tik = T[i][k] + F[i][k]
                tkj = T[k+1][j] + F[k+1][j]
                count=T[i][j]
                if operators[ k ] == "and":
                    T[i][j] += T[i][k] * T[k+1][j]
                    F[i][j] += ( ( tik * tkj ) - T[i][k] * T[k+1][j] )
                elif operators[ k ] == "or":
                    F[i][j] += F[i][k] * F[k+1][j]
                    T[i][j] += ( ( tik * tkj ) - F[i][k] * F[k+1][j] )
                else:
                    T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                    F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]
                if T[i][j]>count:
                    TT[i][j][k]+=T[i][j]-count
            i = i + 1

def createExpression(i,j,symbols,  operators):
    r=" ( "
    for q in range(i,j+1):
        r+=symbols[q]+" "
        if q!=j:
            r+=operators[q]+" "
    r+=" ) "
    return r

def printSolutions(TT,i,j,symbols,  operators):
    if i==j:
        return [" "+symbols[i]+" "]
    result=[]
    for kk in range(((i*2+1)/2),len(symbols)):
        if TT[i][j][kk]>0:
            leftResult=printSolutions(TT,i,kk,symbols,operators)
            rightResult=printSolutions(TT,kk+1,j,symbols,operators)
            if len(leftResult)==0:
                leftResult=[ createExpression(i,kk,symbols,operators) ]
            if len(rightResult)==0:
                rightResult=[ createExpression(kk+1,j,symbols,operators) ]
            resultAll=list(itertools.product(leftResult,rightResult))
                
            for q in resultAll:
                result.append(" ( "+q[0]+operators[kk]+q[1]+" ) ")
    return result
        
                
    
    
def print_matrix( matrix ):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

if __name__ == "__main__":
    Symbols = "TTFT"
    Operators= [ "or" , "and" , "xor" ]
    n = len( Symbols )
    TT=[[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
    T = [ None ] * n
    F = [ None ] * n
    for k in range( len( T ) ) :
        T[ k ] = [ None ] * n
        F[ k ] = [ None ] * n

    parenthesization_iterative( Symbols,  Operators,  n, F, T,TT )

    print "Cantidad de parentizaciones posibles para que la expresion %s sea verdadera: %i" %( Symbols, T[0][n-1] )
    print_matrix( T )
    r= printSolutions(TT,0,len(Symbols)-1,Symbols,  Operators)
    for i in r:
        print i.replace( " and " , " & " ).replace( " or " , " | " ).replace( " xor " , " ^ " )