#include <stdio.h>
double dot (double *A, double *B, int n) {
    double sum = 0;
    for (int i=0; i<n; i++) {
        sum += A[i]*B[i];
    }
    return sum;
}
void function(double *A, double *B, double *n, double c, int l) {
    double dot1 = dot(A, n, l);
    double dot2 = dot(B, n, l);
    if ((dot1 == c) && (dot2 == 0)) {
        printf("The line lies in the plane.");
    }
}
