#include <stdio.h>
#include <math.h>
void cross(double *A, double *B, double *P) {
    P[0] = A[1]*B[2] - A[2]*B[1];
    P[1] = A[2]*B[0] - A[0]*B[2];
    P[2] = A[0]*B[1] - A[1]*B[0];
}
double function(double *A, double *B) {
    double sum = sqrt(pow(A[1]*B[2] - A[2]*B[1], 2) + pow(A[2]*B[0] - A[0]*B[2], 2) + pow(A[0]*B[1] - A[1]*B[0], 2)) + A[0]*B[0] + A[1]*B[1] + A[2]*B[2]; 
    return sum;
}
