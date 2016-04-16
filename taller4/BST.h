#ifndef BST_H
#define BST_H
#include "Node.h"


template< typename T>
class BST {
  private:
    Node<T>* head;
  public:
    BST(){
      head = NULL;
    }
    Node<T>* getHead(){ return head; }
    void  setHead(Node<T>* nHead);
    void buildHuffman( std::priority_queue< Node< T > > queue );
    void preOrder();
    bool find( T value );
};

#include "BST.hxx"
#endif
