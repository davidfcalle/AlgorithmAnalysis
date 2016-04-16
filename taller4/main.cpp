#include <queue>
#include <iostream>
#include <fstream>
#include <map>
#include "BST.h"
#include "Node.h"
#include <math.h>
#include <stdlib.h>
#include <utility>
#include <queue>
#include "Number.h"
#include "optimal.h"
#include <set>

#define  PAIR std::pair< unsigned long , unsigned long >

template< class T>
bool operator < (const Node<T>& lhs, const Node<T>& rhs) {
  return lhs.data > rhs.data; // para que ordene de mayor  menor
}

int main(){

    std::map< unsigned long , unsigned long > histogram;
    std::ifstream in( "archivito.txt", std::ios_base::binary );
    unsigned long x;
    std::priority_queue< Node< Number  > > queue; // el primer valor del pair es la frecuencia y el segundo el vlaor
    std::set< unsigned long  > set;
    long long quemado = 0;
    while( in ){
      in.read( reinterpret_cast< char* >(&x), sizeof( unsigned long ) );
      x = quemado % 530; // quitar esto antes de enviar, es solo para tenerlo medio quemado
      histogram[ x ]++;
      quemado++;
    }

    // inicio del hufffman
    int entra = 0;
    for( std::map< unsigned long , unsigned long >::iterator iterator = histogram.begin(); iterator != histogram.end(); iterator++ ) {
      Node< Number >& node = *( new Node< Number >(  ) );
      node.data.value = iterator->first;
      node.data.occurrence = iterator->second;
      queue.push( node );
      entra++;
    }
    BST< Number >* huffman = new BST< Number >();
    huffman->setHead( new Node< Number >() );
    huffman->buildHuffman( queue );


    ////////////////// fin del huffman ////////////////////////////////////////

    // se saca un vector de valores tiendo en cuenta el orden parcial
    std::map< unsigned long , unsigned long  > optimal;
    for( std::map< unsigned long , unsigned long >::iterator iterator = histogram.begin(); iterator != histogram.end(); iterator++ ) {
      optimal[  iterator->first ] = iterator->second;
    }
    std::map< unsigned long  , std::map< unsigned long  , K > > res = optimal_binary_tree_MI( optimal , optimal );

    /////////////////////// inciio del set /////////////////////////

    for( std::map< unsigned long , unsigned long >::iterator iterator = histogram.begin(); iterator != histogram.end(); iterator++ ) {
      set.insert( iterator->first  );
    }


    ///////////////////// ahora van las busquedas  ////////////////////////////
    for ( unsigned long i = 0; i < 500; i++) {
      Number n;
      n.value = i;
      huffman->find( n );
      res[ i ][ i ];

    }




}
