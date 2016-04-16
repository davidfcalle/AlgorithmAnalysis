#ifndef NUMBER_H
#define  NUMBER_H

class Number {

  public:
    unsigned long occurrence;
    long long value;
    Number(){   }
    friend bool operator < (const Number& l, const Number& r){
        if( l.occurrence == r.occurrence ){
          return l.value >  r.value;
        }
        return l.occurrence < r.occurrence; // keep the same order
    }
    friend bool operator > (const Number& l, const Number& r){
        return l.occurrence > r.occurrence; // keep the same order
    }
    friend bool operator == ( const Number& l, const Number& r){
        return l.value == r.value; // keep the same order
    }
    friend Number operator + (  Number  lhs, const Number& rhs) {
      lhs.occurrence += rhs.occurrence; // reuse compound assignment
      lhs.value = -1;
      return lhs; // return the result by value (uses move constructor)
    }
    friend std::ostream& operator<<(std::ostream& out, const Number& f){
      return out << f.value;
    }
};

#endif
