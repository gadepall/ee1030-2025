#include <stdio.h>
#include <math.h>
void formula(double *P, double *Q, double *R){
    double sum1 = 0, sum2 = 0;
    for (int i=0; i<2; i++) {
        sum1 += pow(P[i] - Q[i], 2);
        sum2 += pow(R[i] - Q[i], 2);
    }
    if (sum1 == sum2) {
        printf("Q is equidistant from P and R.");
    }
}