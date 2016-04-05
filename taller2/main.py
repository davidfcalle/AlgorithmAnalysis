from quick_sort import quick_sort, quick_sort_helper
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge_sort_helper
from timer import count_time
import random
import sys
#----------------------------------------------------------------------------
#Genera un arreglo de tamanio t con numeros enteros aleatorios.
def generate_vector( t ):
  vector = []
  for i in range ( t ):
    vector.append(  random.randint( 0, 10 ) )
  return vector

#----------------------------------------------------------------------------
#Genera un arreglo de tamanio t con numeros enteros ordenados
def generate_ordered_vector( t ):
  vector = []
  for i in range ( t ):
    vector.append( i )
  return vector

def generate_inverse_vector( t ):
    vector = []
    for i in range ( t ):
      vector.append( t - i )
    return vector

#----------------------------------------------------------------------------
# Ejecuta la funcion de ordenamiento functionOrder recibida como parametro para vectores de tamanio i=1,2,....,1x10^4
# Calcula el tiempo que demora ordenando cada arreglo y escribe el resulatdo en un archivo de
# texto con el nombre de filename
def take_data (  function , filename , strategy ):
  file = open ( filename , 'w' )
  for i in  range ( 1, 2000 ):
    S = strategy( i )
    time_taken = count_time( function , S )
    function( S )
    file.write( '%d,%f\n' % ( i, time_taken ) )
  file.close( )


def main():
    sys.setrecursionlimit(100000)
    #take_data( quick_sort_helper , "quick_sort-ordered.csv" , generate_ordered_vector )
    #take_data( quick_sort_helper , "quick_sort-unordered.csv" , generate_inverse_vector )
    take_data( quick_sort_helper , "quick_sort-mixed.csv" , generate_vector )
    #take_data( merge_sort_helper , "merge_sort-mixed.csv" , generate_vector )
    #take_data( merge_sort_helper , "merge_sort-ordered.csv" , generate_ordered_vector )
    #take_data( merge_sort_helper , "merge_sort-unordered.csv" , generate_inverse_vector )
    #take_data( insertion_sort , "insertion_sort-mixed.csv" , generate_vector )
    #take_data( insertion_sort , "insertion_sort-ordered.csv" , generate_ordered_vector )
    #take_data( insertion_sort , "insertion_sort-unordered.csv" , generate_inverse_vector )

if __name__ == '__main__':
    main()
