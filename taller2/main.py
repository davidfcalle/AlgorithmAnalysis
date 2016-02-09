from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timer import count_time

#----------------------------------------------------------------------------
#Genera un arreglo de tamanio t con numeros enteros aleatorios.
def generate_vector( t ):
  vector = []
  for i in range ( t ):
    vector.append(  random.randint( 0, 1000 ) )
  return vector

def generate_ordered_vector( t ):
    vector = []
    for i in range( t ):
        vector.append( i )
    return vector


#----------------------------------------------------------------------------
# Ejecuta la funcion de ordenamiento functionOrder recibida como parametro para vectores de tamanio i=1,2,....,1x10^4
# Calcula el tiempo que demora ordenando cada arreglo y escribe el resulatdo en un archivo de
# texto con el nombre de filename
def take_data (  functionOrder , filename, strategy ):
  file = open ( filename, 'w')
  data = []
  for i in  range ( 1, 10**4 + 1 ):
    S = strategy ( i )
    time_taken =
    data.append({"n": i , })
    file.write( '%d\t %f\n' % ( i, time_taken ) )
  file.close( )


def main():
    S = [7,1, -12, 2,2,32,321,123, -1, 50, 2,3,3,4,34,23,4,32,432,4,32,43,24,32,4,32,432,4,32,43,24,32,4,32,5,3,5433-4-5,435,4,5,4]
    print count_time( merge_sort , S , 0 , len(S) - 1)
    print S

if __name__ == '__main__':
    main()
