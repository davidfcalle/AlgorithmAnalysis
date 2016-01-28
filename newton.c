#include <stdio.h>
#include <math.h>
// compilar gcc newton.c -o  ejecutable -lm


double f(double x, double num){
  return pow(x, 3) - num;
}

double fPrima(double x){
  return 3 * pow(x, 2);
}

double error(double actual, double anterior){
  return fabs( (actual - anterior) / actual);
}
double siguientePaso(double x,double num){
  return x - (f(x, num) / fPrima(x));
}
double  newtonRaphson(double x, double r){
  printf("%lf\n", x );
  double xi = 1, xs, tmp;
  xs = siguientePaso(xi, x);
  while(  error(xs, xi) > r ){  
    xi = xs;
    xs = siguientePaso(xi,x); // x es el num del usuario
  }
  return xs;
}

int main(int argc, char const *argv[]) {
  double r=0, num=0;
  int n=0;
  scanf("%i %lf", &n, &r);
  while(n--){
    scanf("\n%lf", &num); // el \n  es para escapar lo que viene en el buffer
    printf("Resultado : %lf\n", newtonRaphson(num,r) );
  }
  return 0;
}
