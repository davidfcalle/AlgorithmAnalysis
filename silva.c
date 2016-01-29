
#include <stdio.h>
#include <math.h>
int main(int argc, char** argv) {
    int i;
    int N ;
    float tolerancia;
    int entero;
    float f;
    float x_inicial = 1;
    float valor_anterior = 0;
    float valor_actual = 0;
    float error = 0;
    float error_aux = 100;
    printf("Digite el numero N a sacarle la raiz cubica y la tolerancia R trabajar\n ");
    scanf("%d %f", &N ,&tolerancia);
    for (i=0; i<N ; i++){
    scanf("\n%d",&entero);

    printf("error %f tolerancia %f" , error, tolerancia
     while(error <= tolerancia){

    valor_actual = x_inicial - ((pow (x_inicial,3) - entero)/(3*pow (x_inicial,2)));

    error = ((valor_actual - valor_anterior)/valor_actual);

     if (error == 1){
         error = 0;
     }

    if (error < error_aux && error != -1){

        error_aux=error;

    }

    valor_anterior = valor_actual;

    x_inicial = valor_actual;

    }
        printf ("Raiz cubica de %d : %1.22f con un error minimo de %1.5f\n",entero,x_inicial,error_aux);
        x_inicial = 1;
        error_aux = 0;
        error = 0;

    }
    /*for (int i=0; i<N ; i++){
         scanf("%d" ,&entero);
          f = RaizCubica (entero,tolerancia);
          printf ("f: %f\n",f);

    }*/

}
