#include <iostream>
#include <vector>

struct MaxSubArray{
    int low;
    int high;
    int sum;
    int profit;
};

MaxSubArray FindMaxCrossSubArray(std::vector<int> A , int l , int m , int h ){
  int mInf=-9999999, vl = mInf, s = 0, ml , mr , vr= mInf;
  for (int i = m ; i >= l ; i-- ) {
    s += A[ i ];
    if( s > vl ){
      vl = s;
      ml = i;
    }
  }
  s = 0;
  for( int i = m ; i <=  h ; i++ ){
    s += A[ i ];
    if ( s > vr) {
      vr = s;
      mr = i;
    }
  }
  MaxSubArray ret;
  ret.low = ml; ret.high = mr; ret.sum = vl + vr; ret.profit = A[0] - A[mr];
  return ret;
}

MaxSubArray FindMaxSubArray(std::vector<int> A, int l , int h ){
  MaxSubArray ret;
  int m;
  if( h <= l ){
    //std::cout << "if" << std::endl;
    ret.low = l; ret.high = h; ret.sum = A[ l ]; ret.profit = A[ 0 ] - A[ h ];
    return ret;
  }else{
    //std::cout << "else" << std::endl;
    m = ( l + h ) / 2;
    MaxSubArray la = FindMaxSubArray( A , l , m);
    MaxSubArray ra = FindMaxSubArray( A , m + 1 , h );
    //std::cout << "llega" << std::endl;
    MaxSubArray ca = FindMaxCrossSubArray( A, l , m , h );
    //std::cout << "else -- if" << std::endl;
    if( la.sum >= ra.sum ){
      return la;
    }else if( ra.sum >= la.sum && ra.sum >= ca.sum ){
      return ra;
    }else{
      return ca;
    }
  }
}





int main(int argc, char const *argv[]) {
  std::vector<int> v;
  v.push_back(1);v.push_back(1);v.push_back(1);v.push_back(5);v.push_back(1);v.push_back(-1);v.push_back(1); v.push_back(-5);
  MaxSubArray result = FindMaxSubArray( v , 0 , v.size());
  std::cout<< result.low << " " << result.high << " " << result.sum <<std::endl;
  return 0;
}
