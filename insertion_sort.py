import time
import random

def insertion_sort(S):
    for j in range ( 1 , len(S) ):
        k = S[j]
        i = j - 1
        while( i > 0 and S[i] > k):
            S[ i + 1 ] = S[ i ]
            i = i - 1
        S[ i + 1 ] = k
    return S

#----------------------------------------------------------------------------
#Genera un arreglo de tamanio t con numeros enteros aleatorios.
def generate_vector( t ):
  vector = []
  for i in range ( t ):
    vector.append(  random.randint( 0, 1000 ) )
  return vector


#----------------------------------------------------------------------------
# Ejecuta la funcion de ordenamiento functionOrder recibida como parametro para vectores de tamanio i=1,2,....,1x10^4
# Calcula el tiempo que demora ordenando cada arreglo y escribe el resulatdo en un archivo de
# texto con el nombre de filename
def take_data (  functionOrder, filename ):
  file = open ( filename, 'w')
  for i in  range ( 1, 10**4 +1 ):
    vector = generate_vector ( i )
    t0 = time.clock( )
    functionOrder ( vector )
    file.write( '%d\t %f\n' % ( i, time.clock( )  - t0 ) )
  file.close( )


if __name__ == '__main__':
    take_data( insertion_sort , "InsertionSort.txt" )
