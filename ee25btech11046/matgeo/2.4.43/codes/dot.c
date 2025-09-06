#include <stdio.h>
#include <math.h>
double dot(double *A, double *B, int m) {
    double dot=0;
    for ( int i = 0 ; i < m ; i++ ) {
        dot += A[i]*B[i] ; 
    }
    return dot;
}
