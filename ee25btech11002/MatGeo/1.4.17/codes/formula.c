#include <stdio.h>
void section_formula(float *P, float *A, float *B, int m, int n, int k){
for (int i = 0; i < k ; i++) {
    P[i] = (m*B[i]+n*A[i])/(m+n);
}
}
