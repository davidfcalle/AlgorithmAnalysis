#ifndef NODE_H
#define NODE_H

template <typename T>
class Node{
  public:
    Node(){
      left = NULL;
      right = NULL;
    }
    Node( T ndata){
      data = ndata;
      left = NULL;
      right = NULL;
    }

    T   data;
    Node<T>* left;
    Node<T>* right;
    void setData( T data );
    T getData();
    void preOrder();
    bool findN( T value ){
      bool l = false;
      bool r = false;
      if( left != NULL ){
        l = left->findN( data );
      }
      if( right != NULL ){
        r = right->findN( data );
      }
      if( r ){
        return true;
      }
      return false;
    }


    friend Node<T> operator + ( Node<T> lhs, const Node<T>& rhs) {
      lhs.data = lhs.data + rhs.data; // reuse compound assignment
      return lhs; // return the result by value (uses move constructor)
    }
    friend std::ostream& operator<<(std::ostream& out, const Node& f){
      return out << f.data;
    }

};
#include "Node.hxx"
#endif
