#include "Node.h"
template <typename T>
void Node<T>::preOrder(){

  std::cout<< data << std::endl;
  if( left != NULL ){
    left->preOrder();
  }

  if( right != NULL ){
    right->preOrder();
  }

}
