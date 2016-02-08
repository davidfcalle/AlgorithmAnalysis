from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
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
def take_data (  functionOrder , filename ):
  file = open ( filename, 'w')
  for i in  range ( 1, 10**4 +1 ):
    vector = generate_vector ( i )
    t0 = time.clock( )
    functionOrder ( vector )
    file.write( '%d\t %f\n' % ( i, time.clock( )  - t0 ) )
  file.close( )


def main():
    S = [7,1, -12, 2,2,32,321,123, -1]
    print S
    merge_sort( S , 0 , len( S ) - 1 )
    print S

if __name__ == '__main__':
    main()
