#include <stdio.h>
#include <math.h>
void function(double *P, double *B, double *A , int m, int k) {
    for ( int i = 0 ; i < m ; i++ ) {
        P[i] = (1*A[i] + k*B[i])/(k+1) ; 
    }
}
