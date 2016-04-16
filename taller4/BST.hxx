#include "BST.h"

template< typename T>
void  BST<T>::setHead(Node<T>* nHead){
  head = nHead;
};
//void buildHuffman( std::priority_queue< Node< T > > queue );
template< typename T>
void BST<T>::buildHuffman( std::priority_queue< Node< T > > queue ){
  while ( queue.size() > 1 ){
      Node< T > tfirst = queue.top(); queue.pop();
      //std::cout << " se saca uno con valor "<< tfirst <<std::endl;
      Node< T > tsecond = queue.top(); queue.pop();
      Node< T > tparent;
      Node< T >& first = *( new Node< T >( tfirst.data ) );
      first.left = tfirst.left; first.right = tfirst.right;
      Node< T >& second = *( new Node< T >( tsecond.data ) );
      second.left = tsecond.left; second.right = tsecond.right;
      tparent = first + second;
      Node< T >& parent = *( new Node< T >( tparent.data ) );
      parent.left = &first; parent.right = &second;
      //std::cout<< "queda padre  "<< parent << " izquierda " << *parent.left  << " derecha "<< *parent.right << std::endl;
      queue.push( parent );
  }
  //std::cout<<" quedan en la cola "<< queue.size() <<std::endl;
  Node<T> tnewHead = queue.top();
  Node<T>& newHead = *( new Node< T >( tnewHead.data ) );
  newHead.left = tnewHead.left; newHead.right = tnewHead.right;
  //std::cout << head->left << " --- " << head->right <<std::endl;
  head = &newHead;
  //head->preOrder();
}


template< typename T>
void  BST<T>::preOrder(){
  if( head != NULL ){
    head->preOrder();
  }
};

template< typename T>
bool  BST<T>::find( T value ){
  if( head != NULL ){
    return head->findN( value );
  }
  return false;
};
