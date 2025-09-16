#include <stdio.h>
#include <math.h>
double dot(double *A, double *B) {
    double sum = A[0]*B[0] + A[1]*B[1] + A[2]*B[2];
    return sum;
}
double triple_product(double *A, double *B, double *C) {
    double sum = A[0]*(B[1]*C[2] - B[2]*C[1]) + A[1]*(B[2]*C[0] - B[0]*C[2]) + A[2]*(B[0]*C[1] - B[1]*C[0]);
    return sum;
}
double function(double *A, double *B, double *C, double *X) {
    if ((dot(A, X) == 0) && (dot(B, X) == 0) && (dot(C, X) == 0)) {
        double value = triple_product(A, B, C);
        return value;
    }
}
